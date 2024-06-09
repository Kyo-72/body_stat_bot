import json
import os
import requests

def fetch_health_data_a_week():
    # URL
    url = os.getenv('HEALTH_API_URL')

    # POSTデータ
    data = {
        'access_token': os.getenv('HEALTH_API_ACCESS_TOKEN'),
        'date': '1',
        'from': '20240409000000',
        'to': '20240609235959',
        'tag': '6021,6022'
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

# この関数を直接実行してテストする場合のコード（ローカルでのテスト用）
if __name__ == "__main__":
    result = fetch_health_data_a_week()
    print(result)
