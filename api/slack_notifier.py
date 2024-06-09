import json
import os
import requests

def notify_slack_channel():
    # Slack Webhook URL
    url = os.getenv('SLACK_URL')
    
    # メッセージのデータ
    payload = {
        "text": "なんかおくれや"
    }
    
    # リクエストを送信
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # HTTPエラーが発生した場合に例外をスロー
        
        result = {
            "message": "メッセージが送信されました",
            "response": response.text
        }
    except requests.exceptions.HTTPError as e:
        result = {
            "error": f"エラーが発生しました: {e.response.status_code}",
            "response": e.response.text
        }
    
    # 結果をJSON形式で返す
    return {
        'statusCode': 200 if 'message' in result else 500,
        'body': json.dumps(result, ensure_ascii=False)
    }
