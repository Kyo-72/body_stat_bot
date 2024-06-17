from api.slack_notifier import notify_slack_channel
from db_layer.database import get_session
from datetime import datetime, timedelta
from logic.average_health_data_calc import calculate_daily_average_health_data, calculate_average_health_data_for_period
from logic.message.message import create_message
from repository.health_data_repository import HealthDataRepository
from transformers.db.health_data_transformer import transform_db_health_data
from transformers.db.health_data_transformer import transform_db_health_data
from transformers.db.health_data_transformer import transform_db_health_data
from pprint import pprint

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
    # データを整形  
    transformed_health_data_list = transform_db_health_data(health_data_list)
    # 日別測定データをDBに入れるならここらでDBに保存しないといけないね
    # 日毎の平均値を計算
    #TODO ここら辺のロジック、完全に分離した方がいいかもね
    daily_average_health_data = calculate_daily_average_health_data(transformed_health_data_list)
    # daily_average_health_dataに含まれる各日の平均体重と平均体脂肪率から、全期間の平均体重と平均体脂肪率を計算する
    average_health_data_for_period = calculate_average_health_data_for_period(daily_average_health_data)
    #TODO メッセージを作成
    message_for_slack = create_message(average_health_data_for_period)
    #TODO slackで通知
    notify_slack_channel(message_for_slack)

notify_weekly_average_weight()