from datetime import date, timedelta

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