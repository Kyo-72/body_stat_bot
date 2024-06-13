from datetime import date, timedelta

def calculate_daily_average_health_data(transformed_health_data: dict) -> dict:
    '''
    日毎の平均データを計算する
    
    '''
    daily_average_health_data_list = []
    for health_date in transformed_health_data:
        daily_average_health_data = {'date' : health_date['date'], 'avr_weight': None, 'avr_bfp': None}
        daily_average_health_data['avr_weight'] = _calculate_daily_health_data(health_date['weight_list'])
        daily_average_health_data['avr_bfp'] = _calculate_daily_health_data(health_date['bfp_list'])
        daily_average_health_data_list.append(daily_average_health_data)

    return daily_average_health_data_list

def _calculate_daily_health_data(data_list: list) -> float:
    data_sum = 0.0
    num_of_data = len(data_list)
    for data in data_list:
        data_sum += data
    avr_data = data_sum/num_of_data

    return avr_data