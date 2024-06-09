import datetime
from models.my_health_data import MyHealthData
from sqlalchemy.orm import Session

def bulk_insert_health_data(db: Session, data_list: list):
    """
    複数のMyHealthDataレコードを一度に挿入する関数
    """
    new_records = []
    for data in data_list:
        #重複するデータはDBに入れない
        if( check_existing_measurement_datetime(db, data['measurement_datetime']) ):
            continue

        new_records.append( MyHealthData(
                weight=data['weight'],
                bfp=data['bfp'],
                measurement_datetime=data['measurement_datetime']
            )
        )
    
    db.bulk_save_objects(new_records)
    db.commit()
    return new_records

def check_existing_measurement_datetime(db: Session, measurement_datetime: datetime) -> bool:
    """
    同一のmeasurement_datetimeが存在するか確認する関数
    """
    return db.query(MyHealthData).filter(
        MyHealthData.measurement_datetime == measurement_datetime
    ).first() is not None

def get_health_data_by_period(db: Session, start_date: datetime, end_date: datetime):
    """
    指定期間のMyHealthDataレコードを取得する関数
    """
    return db.query(MyHealthData).filter(
        MyHealthData.measurement_datetime >= start_date,
        MyHealthData.measurement_datetime <= end_date
    ).all()