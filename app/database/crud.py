from sqlalchemy.orm import Session
from models.my_health_data import MyHealthData

def insert_health_data(db: Session, weight: float, bfp: float, measurement_datetime):
    """
    単一のMyHealthDataレコードを挿入する関数
    """
    new_record = MyHealthData(
        weight=weight,
        bfp=bfp,
        measurement_datetime=measurement_datetime
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def bulk_insert_health_data(db: Session, data_list: list):
    """
    複数のMyHealthDataレコードを一度に挿入する関数
    """
    new_records = [
        MyHealthData(
            weight=data['weight'],
            bfp=data['bfp'],
            measurement_datetime=data['measurement_datetime']
        ) for data in data_list
    ]
    db.bulk_save_objects(new_records)
    db.commit()
    return new_records