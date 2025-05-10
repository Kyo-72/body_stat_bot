import datetime
import json
from typing import Any, Dict

def transform_health_api_data(json_data: Dict[str, Any]) -> dict:
    data_list = _deserialize_health_data(json_data)
    _format_datetime(data_list)
    squashed_data_dict = _squash_data(data_list)
    return squashed_data_dict

def _deserialize_health_data(data: Dict[str, Any]) -> list:
    """
    JSONからPythonオブジェクトにするだけ
    """
    #TODO HTTPエラーが出た時の対処
    outer_body = json.loads(data['body'])
    # inner_body = json.loads(outer_body['body'])
    data_list = outer_body['data']
    return data_list

def _format_datetime(data_list: list) -> None:
    """
    元データのdateは文字列。DBに格納するため、datetimeオブジェクトに変換
    """
    for data in data_list:
        data['date'] = datetime.datetime.strptime(data['date'], "%Y%m%d%H%M")

def _squash_data(data_list: list) -> dict:
    """
    元のデータは体重と体脂肪率が別のデータで与えられるので、測定日ごとにまとめてdictで返す
    """
    squashed_data_dict = {}
    for data in data_list:
        date = data['date']
        tag = data['tag']
        key_data = float(data['keydata'])  # key_dataはfloatに変換

        if date not in squashed_data_dict:
            squashed_data_dict[date] = {'weight': None, 'bfp': None}

        if tag == '6021':
            squashed_data_dict[date]['weight'] = key_data
        elif tag == '6022':
            squashed_data_dict[date]['bfp'] = key_data

    return squashed_data_dict
