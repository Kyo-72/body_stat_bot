import datetime
import json
import requests
import string
from param_store import get_param

def fetch_health_data_by_date_range(start_datetime : datetime, end_datetime: datetime) ->json:
    # URL
    url = get_param('HEALTH_API_URL')

    # POSTデータ
    data = {
        'access_token': get_param('HEALTH_API_ACCESS_TOKEN'),
        'date'        : '1',
        'from'        : datetime_to_string(start_datetime),
        'to'          : datetime_to_string(end_datetime),
        'tag'         : '6021,6022'                           #6021 体重、 6022 体脂肪率
    }

    # ヘッダー
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        # リクエストを送信してレスポンスを取得
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # HTTPエラーが発生した場合に例外をスロー

        result = {
            'statusCode': 200,
            'body': response.text
        }
    except requests.exceptions.HTTPError as e:
        result = {
            'statusCode': e.response.status_code,
            'body': e.response.text
        }
    except requests.exceptions.RequestException as e:
        result = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    # 結果をJSON形式で返す
    return result

def datetime_to_string(datetime: datetime) ->string:
    return datetime.strftime('%Y%m%d%H%M%S')
