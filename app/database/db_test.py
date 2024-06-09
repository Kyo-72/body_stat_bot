from database import engine, Base, get_session
from datetime import datetime, timedelta
from repository.health_data import HealthDataRepository
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

with next(get_session()) as session:
    repository = HealthDataRepository(session)
    
    # # データの一括挿入
    # data_list = [
    #     {'weight': 70.5, 'bfp': 20.0, 'measurement_datetime': datetime(2023, 6, 10, 12, 0, 0)},
    #     {'weight': 71.0, 'bfp': 19.8, 'measurement_datetime': datetime(2023, 6, 11, 12, 0, 0)},
    #     # 他のデータ...
    # ]
    # new_records = repository.bulk_insert_health_data(data_list)
    # for record in new_records:
    #     print(record)

    # 指定期間のデータ取得
    start_date = datetime(2024, 6, 1)
    end_date = datetime(2024, 6, 30)
    health_data = repository.get_health_data_by_period(start_date, end_date)
    for data in health_data:
        print(vars(data))



# データベースを作る処理
# Base.metadata.create_all(bind=engine)   