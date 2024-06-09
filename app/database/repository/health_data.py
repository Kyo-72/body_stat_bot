import datetime
from models.my_health_data import MyHealthData
from sqlalchemy.orm import Session

class HealthDataRepository:
    def __init__(self, db: Session):
        self.db = db

    def bulk_insert_health_data(self, data_list: list):
        """
        複数のMyHealthDataレコードを一度に挿入する関数
        """
        new_records = []
        for data in data_list:
            # 重複するデータはDBに入れない
            if self.__check_existing_measurement_datetime(data['measurement_datetime']):
                continue

            new_records.append(MyHealthData(
                    weight=data['weight'],
                    bfp=data['bfp'],
                    measurement_datetime=data['measurement_datetime']
                )
            )
        
        self.db.bulk_save_objects(new_records)
        self.db.commit()
        return new_records

    def __check_existing_measurement_datetime(self, measurement_datetime: datetime) -> bool:
        """
        同一のmeasurement_datetimeが存在するか確認する関数
        """
        return self.db.query(MyHealthData).filter(
            MyHealthData.measurement_datetime == measurement_datetime
        ).first() is not None

    def get_health_data_by_period(self, start_date: datetime, end_date: datetime):
        """
        指定期間のMyHealthDataレコードを取得する関数
        """
        return self.db.query(MyHealthData).filter(
            MyHealthData.measurement_datetime >= start_date,
            MyHealthData.measurement_datetime <= end_date
        ).all()
