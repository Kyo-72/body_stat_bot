from database import engine, Base, get_session
from datetime import datetime
from crud import insert_health_data, bulk_insert_health_data
from sqlalchemy.orm import Session
from models.my_health_data import MyHealthData

# セッションの取得
# with next(get_session()) as session:
#     new_record = insert_health_data(session, 70.5, 20.0, datetime.now())
#     print(new_record)

# 挿入するデータのリスト
data_list = [
    {'weight': 70.5, 'bfp': 20.0, 'measurement_datetime': datetime.now()},
    {'weight': 71.0, 'bfp': 19.8, 'measurement_datetime': datetime.now()},
    # 他のデータ...
]

# セッションの取得
with next(get_session()) as session:
    new_records = bulk_insert_health_data(session, data_list)
    for record in new_records:
        print(record)


# データベースを作る処理
# Base.metadata.create_all(bind=engine)   