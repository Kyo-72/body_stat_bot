import json
import requests
from param_store import get_param

def notify_slack_channel(message):
    # Slack Webhook URL
    url = get_param('SLACK_URL')
    
    # メッセージのデータ
    payload = {
        'text': message
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
