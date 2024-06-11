from db_layer.database import engine, Base, get_session

from api.health_data_api import fetch_health_data_by_date_range
from datetime import datetime, timedelta

from repository.health_data_repository import HealthDataRepository


def fetch_and_store_daily_data():
    yesterday = datetime.now() - timedelta(days = 1)
    today     = datetime.now()
    #TODO Tanita Health Planet APIから一日分のデータを取得する
    health_data = fetch_health_data_by_date_range(yesterday, today)
    #TODO DB　にbulk insertする
    with next(get_session()) as session:
        repository = HealthDataRepository(session)

    return True


fetch_and_store_daily_data()