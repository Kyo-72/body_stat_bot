from api.slack_notifier import notify_slack_channel
from logic.average_health_data_calc import calculate_daily_average_health_data, calculate_average_health_data_for_period
from logic.message.message import create_message
from services.health_data_service import HealthDataService
from repositories.health_data_repository import HealthDataRepository
from transformers.db.health_data_transformer import transform_db_health_data
from transformers.db.health_data_transformer import transform_db_health_data
from transformers.db.health_data_transformer import transform_db_health_data
from pprint import pprint

def notify_weekly_average_weight():
    #DBからデータを取得
    health_data_list = []
    health_data_service = HealthDataService();
    # ここで指定した週間分のデータを取得(10/22)
    health_data_list = health_data_service.fetch_health_data_by_weeks(weeks = 1)
    # データを整形  
    # TODO トランスフォームじゃなくてhealth_dataのサービスでいい
    transformed_health_data_list = transform_db_health_data(health_data_list)

    if len(transformed_health_data_list) == 0:
        return
    # 日別測定データをDBに入れるならここらでDBに保存しないといけないね
    # 日毎の平均値を計算
    # ここら辺のロジック、完全に分離した方がいいかもね
    # ここらはドメインぽいからいいかもやけどサービスから呼び出すのがいいかな
    daily_average_health_data = calculate_daily_average_health_data(transformed_health_data_list)
    # daily_average_health_dataに含まれる各日の平均体重と平均体脂肪率から、全期間の平均体重と平均体脂肪率を計算する
    average_health_data_for_period = calculate_average_health_data_for_period(daily_average_health_data)
    # メッセージを作成
    message_for_slack = create_message(average_health_data_for_period)
    print(message_for_slack)
    # slackで通知
    notify_slack_channel(message_for_slack)

notify_weekly_average_weight()