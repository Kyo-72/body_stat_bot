import datetime
from db_layer.models.my_health_data import MyHealthData
from db_layer.database import get_session

class HealthDataRepository:

    def bulk_insert_health_data(self, data_dict: dict):
        """
        複数のMyHealthDataレコードを一度に挿入する関数
        """
        with get_session() as db:  # セッションをリポジトリ内で管理
            new_records = []
            for datetime, health_data in data_dict.items():
                # 重複するデータはDBに入れない
                if self.__check_existing_measurement_datetime(db, datetime):
                    continue

                new_records.append(MyHealthData(
                        weight               = health_data['weight'],
                        bfp                  = health_data['bfp'],
                        measurement_datetime = datetime
                    )
                )
            
            db.bulk_save_objects(new_records)
            db.commit()
        return new_records

    def __check_existing_measurement_datetime(self, db, measurement_datetime: datetime) -> bool:
        """
        同一のmeasurement_datetimeが存在するか確認する関数
        """
        return db.query(MyHealthData).filter(
            MyHealthData.measurement_datetime == measurement_datetime
        ).first() is not None

    def get_health_data_by_period(self, start_date: datetime, end_date: datetime):
        """
        指定期間のMyHealthDataレコードを取得する関数
        """
        with get_session() as db:  # セッションをリポジトリ内で管理
            return db.query(MyHealthData).filter(
                MyHealthData.measurement_datetime >= start_date,
                MyHealthData.measurement_datetime <= end_date
            ).all()

    def delete_health_data_before(self, cutoff_datetime: datetime):
        """
        指定期間以前のMyHealthDataレコードを削除する関数
        """
        with get_session() as db:  # セッションをリポジトリ内で管理
            db.query(MyHealthData).filter(
                MyHealthData.measurement_datetime <= cutoff_datetime
            ).delete(synchronize_session=False)
            db.commit()
