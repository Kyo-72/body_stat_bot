from api.slack_notifier import notify_slack_channel
from logic.average_health_data_calc import calculate_daily_average_health_data, calculate_average_health_data_for_period
from logic.message.message import create_message
from services.health_data_service import HealthDataService
from repositories.health_data_repository import HealthDataRepository
from transformers.db.health_data_transformer import transform_health_data_by_date
from pprint import pprint
from datetime import datetime, timedelta

def notify_weekly_average_weight():
    
    # ────────────────────────────────────────────────
    # 「今週」
    # ────────────────────────────────────────────────
    now = datetime.now()
    this_week_start = (
        now - timedelta(days=7)
        ).replace(hour=0, minute=0, second=0, microsecond=0)
    this_week_end = now 
    # ────────────────────────────────────────────────
    # 「先週」
    # ────────────────────────────────────────────────
    # ちょうど7日前の0:00
    last_week_start = (now - timedelta(days=14)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    last_week_end = (now - timedelta(days=7)).replace(
        hour=0, minute=0, second=0, microsecond=0
    ) - timedelta(seconds=1)

    service = HealthDataService()

    this_week_data = service.fetch_health_data_by_period(
        start_datetime=this_week_start,
        end_datetime=this_week_end,
    )

    # 今週分の測定データがない場合は中止
    if len(this_week_data) == 0:
        return
    
    average_daily_data_this_week = __calc_daily_average(this_week_data)
    average_weekly_data_this_week = __calc_weekly_average(average_daily_data_this_week)

    last_week_data = service.fetch_health_data_by_period(
        start_datetime=last_week_start,
        end_datetime=last_week_end,
    )
    average_daily_data_last_week = {}
    average_weekly_data_last_week = []

    # 先週の測定データがない場合は平均を求める処理をスキップスキップ
    if not len(last_week_data) == 0:
        average_daily_data_last_week = __calc_daily_average(last_week_data)
        average_weekly_data_last_week  = __calc_weekly_average(average_daily_data_last_week)
    
    # メッセージを作成
    message_for_slack = create_message(
        average_daily_data_this_week,
        average_daily_data_last_week,
        average_weekly_data_this_week,
        average_weekly_data_last_week
        )
    print(message_for_slack)
    # slackで通知
    res = notify_slack_channel(message_for_slack)
    print(res)

def __calc_daily_average(date_list):
    health_datum_by_date = transform_health_data_by_date(date_list)
    return calculate_daily_average_health_data(health_datum_by_date)

def __calc_weekly_average(daily_average):
    # daily_average_health_dataに含まれる各日の平均体重と平均体脂肪率から、全期間の平均体重と平均体脂肪率を計算する
    return calculate_average_health_data_for_period(daily_average)
    
notify_weekly_average_weight()