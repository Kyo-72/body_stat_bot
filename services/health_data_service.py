from datetime import datetime, timedelta
from repositories.health_data_repository import HealthDataRepository

class HealthDataService:

    def __init__(self):
        self.repository = HealthDataRepository()

    #相対指定（週数）
    def fetch_health_data_by_weeks(self, weeks: int = 1):
        end_datetime = datetime.now()
        start_datetime = end_datetime - timedelta(days=7 * weeks)
        return self.fetch_health_data_by_period(start_datetime, end_datetime)

    # 絶対指定（開始日・終了日）
    def fetch_health_data_by_period(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
    ):
        if start_datetime > end_datetime:
            raise ValueError("start_datetime must be earlier than end_datetime")
        return self.repository.get_health_data_by_period(start_datetime, end_datetime)