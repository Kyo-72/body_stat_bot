from datetime import datetime, timedelta
from repositories.health_data_repository import HealthDataRepository

class HealthDataService:

    def __init__(self):
        self.repository = HealthDataRepository()

    def fetch_health_data_by_weeks(self, weeks=1):
        # 一週間のデータを
        start_datetime = datetime.now() - timedelta(days = 7 * weeks)
        end_datetime   = datetime.now()
        
        health_data_list = self.repository.get_health_data_by_period(start_datetime, end_datetime)

        return health_data_list