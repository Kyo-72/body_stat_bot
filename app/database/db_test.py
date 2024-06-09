from database import engine, Base, get_session
from datetime import datetime, timedelta
from crud import bulk_insert_health_data, get_health_data_by_period
from sqlalchemy.orm import Session
from models.my_health_data import MyHealthData
import pprint

# セッションの取得
# with next(get_session()) as session:
#     new_record = insert_health_data(session, 70.5, 20.0, datetime.now())
#     print(new_record)

# 挿入するデータのリスト
data_list = [
    {'weight': 70.5, 'bfp': 20.0, 'measurement_datetime': datetime(2020, 8, 21)},
    {'weight': 71.0, 'bfp': 19.8, 'measurement_datetime': datetime.now()},
    # 他のデータ...
]

# セッションの取得
with next(get_session()) as session:
    new_records = bulk_insert_health_data(session, data_list)
    for record in new_records:
        print(record)

# with next(get_session()) as session:
#     start_date = datetime.now() - timedelta(days=7)
#     end_date = datetime.now()
#     health_data = get_health_data_by_period(session, start_date, end_date)
#     for data in health_data:
#         print(vars(data))


# データベースを作る処理
# Base.metadata.create_all(bind=engine)   