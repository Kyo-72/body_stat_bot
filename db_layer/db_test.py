from database import engine, Base, get_session
from datetime import datetime, timedelta
from repositories.health_data_repository import HealthDataRepository
from transformers.jsons.health_data_transformer import deserialize_to_dict_from_json
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
]

# with next(get_session()) as session:
#     repository = HealthDataRepository(session)
    
    # # データの一括挿入
    # new_records = repository.bulk_insert_health_data(data_list)
    # for record in new_records:
    #     print(record)

    # 指定期間のデータ取得
    # start_date = datetime(2024, 6, 1)
    # end_date = datetime(2024, 6, 30)
    # health_data = repository.get_health_data_by_period(start_date, end_date)
    # for data in health_data:
    #     print(vars(data))

    #指定期間以前のdbを消す
    # cutoff_datetime = datetime.now() - timedelta(hours=1)
    # repository.delete_health_data_before(cutoff_datetime)

    # data_dict   = deserialize_to_dict_from_json(sample_data)
    # new_records = repository.bulk_insert_health_data(data_dict)
    # for record in new_records:
    #     print(record)



# データベースを作る処理
Base.metadata.create_all(bind=engine)   

with next(get_session()) as session:
    repository = HealthDataRepository(session)
    # 挿入するデータのリスト
    sample_data = {'statusCode': 200, 'body': '{"health_data_result": {"statusCode": 200, "body": "{\\"birth_date\\":\\"19990702\\",\\"data\\":[{\\"date\\":\\"202406022002\\",\\"keydata\\":\\"83.60\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6021\\"},{\\"date\\":\\"202406022002\\",\\"keydata\\":\\"27.70\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6022\\"},{\\"date\\":\\"202406011909\\",\\"keydata\\":\\"83.00\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6021\\"},{\\"date\\":\\"202406011909\\",\\"keydata\\":\\"25.90\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6022\\"},{\\"date\\":\\"202405301608\\",\\"keydata\\":\\"84.30\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6021\\"},{\\"date\\":\\"202405301608\\",\\"keydata\\":\\"26.20\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6022\\"},{\\"date\\":\\"202405291539\\",\\"keydata\\":\\"83.70\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6021\\"},{\\"date\\":\\"202405291539\\",\\"keydata\\":\\"25.60\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6022\\"},{\\"date\\":\\"202405290039\\",\\"keydata\\":\\"84.20\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6021\\"},{\\"date\\":\\"202405290039\\",\\"keydata\\":\\"25.90\\",\\"model\\":\\"01000145\\",\\"tag\\":\\"6022\\"}],\\"height\\":\\"173\\",\\"sex\\":\\"male\\"}"}}'}

    data_dict   = deserialize_to_dict_from_json(sample_data)
    new_records = repository.bulk_insert_health_data(data_dict)
