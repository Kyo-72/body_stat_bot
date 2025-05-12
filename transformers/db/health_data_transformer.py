from db_layer.models.my_health_data import MyHealthData
from datetime import datetime

def transform_health_data_by_date(health_data_list: list[MyHealthData]) -> dict:
    '''
    データを測定日時日時毎に整形する
    input
    output : { date : {'weigh' : [float], 'bfp' : [float]} }
    '''
    daily_health_data_json = {}

    for daily_health_data in health_data_list:
        date   = daily_health_data.measurement_datetime.date()
        weight = daily_health_data.weight
        bfp    = daily_health_data.bfp
        # 日毎のデータが存在していなければリストとしてhealth_dataを登録
        if date not in daily_health_data_json:
            daily_health_data_json[date] = {
                'weight_list' : [float(weight)],
                'bfp_list'   : [float(bfp)]
            }
        else :
        # すでに登録されている場合はlistに追加
            daily_health_data_json[date]['weight_list'].append(float(weight))
            daily_health_data_json[date]['bfp_list'].append(float(bfp))

    return daily_health_data_json
