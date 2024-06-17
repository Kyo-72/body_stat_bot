from datetime import date
from typing import List, Tuple, Optional

def calculate_daily_average_health_data(transformed_health_data: dict) -> dict:
    '''
    日毎の平均データを計算する
    input : 
    
    '''
    daily_average_health_data = {}
    for date, health_date in transformed_health_data.items():
        daily_average_health_data[date] = {'avr_weight' : None, 'avr_bfp' : None}
        daily_average_health_data[date]['avr_weight'] = _calculate_daily_health_data(health_date['weight_list'])
        daily_average_health_data[date]['avr_bfp'] = _calculate_daily_health_data(health_date['bfp_list'])

    return daily_average_health_data

def _calculate_daily_health_data(data_list: list) -> float:
    data_sum = 0.0
    num_of_data = len(data_list)
    for data in data_list:
        data_sum += data
    avr_data = data_sum/num_of_data

    return avr_data

def calculate_average_health_data_for_period(daily_average_health_data: dict):
    
    date_list = daily_average_health_data.keys()
    start_date, end_date = _set_start_date_and_end_date(date_list)

    num_of_date = len(date_list)
    health_data_list = daily_average_health_data.values()

    sum_weight = sum([health_data['avr_weight'] for health_data in health_data_list])
    sum_bfp    = sum([health_data['avr_bfp'] for health_data in health_data_list])

    avr_weight = sum_weight / num_of_date
    avr_bfp    = sum_bfp / num_of_date

    return {'start_date' : start_date, 'end_date' : end_date, 'avr_weight' : round(avr_weight, 2), 'avr_bfp' : round(avr_bfp, 2)}

def _set_start_date_and_end_date(date_list: list) -> Tuple[Optional[date], Optional[date]]:
    start_date = None
    end_date   = None
    for date in date_list:
        start_date = date if start_date == None or (date < start_date) else start_date
        end_date = date if end_date == None or (date > end_date) else end_date

    return start_date, end_date