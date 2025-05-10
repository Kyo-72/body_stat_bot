from api.health_data_api import fetch_health_data_by_date_range
from datetime import datetime, timedelta
from db_layer.database import get_session
from repositories.health_data_repository import HealthDataRepository
from transformers.jsons.health_data_transformer import transform_health_api_data


def fetch_and_store_daily_data():
    yesterday = datetime.now() - timedelta(days = 7)
    today     = datetime.now()
    # Tanita Health Planet APIから一日分のデータを取得する
    health_data = fetch_health_data_by_date_range(yesterday, today)
    transformed_health_data = transform_health_api_data(health_data)
    #DB　にbulk insertする 
    #TODO ここでrepository触るのは正しいの?かを検討する
    repository = HealthDataRepository()

    if transformed_health_data == {}:
        #TODO 適切な返り値について考える
        return False
    repository.bulk_insert_health_data(transformed_health_data)

    #TODO 適切な返り値について考える
    print('hoge')
    return True

fetch_and_store_daily_data();