from db_layer.database import get_session
from datetime import datetime, timedelta
from repository.health_data_repository import HealthDataRepository
from transformers.db.health_data_transformer import transform_db_health_data
from transformers.db.health_data_transformer import transform_db_health_data

def notify_weekly_average_weight():
    #TODO これがここにあるの良くないかも
    start_datetime = datetime.now() - timedelta(days = 50)
    end_datetime   = datetime.now()
    #DBからデータを取得
    health_data_list = []
    #TODO ここでrepository触るのは正しいの?かを検討する
    with next(get_session()) as session:
        repository = HealthDataRepository(session)
        health_data_list = repository.get_health_data_by_period(start_datetime, end_datetime)
    #TODO データを整形  
    transfromed_health_data_list = transform_db_health_data(health_data_list)
    #TODO データを整形  
    transfromed_health_data_list = transform_db_health_data(health_data_list)
    #TODO 日別測定データをDBに入れるならここらでDBに保存しないといけないね
    #TODO 平均値を計算
    #TODO メッセージを作成
    #TODO slackで通知
    pass

notify_weekly_average_weight()

notify_weekly_average_weight()