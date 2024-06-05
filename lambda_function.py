import json
from health_data_api import fetch_health_data_a_week
from slack_notifier import notify_slack_channel

def lambda_handler(event, context):
    health_data_result = fetch_health_data_a_week()
    slack_result = notify_slack_channel()
    result = {
        'statusCode': 200,
        'body': json.dumps({
            'health_data_result': health_data_result,
            # 'slack_result': slack_result
        }, ensure_ascii=False)
    }

    return result


# この関数を直接実行してテストする場合のコード（ローカルでのテスト用）
if __name__ == "__main__":
    event = {}
    context = {}
    result = lambda_handler(event, context)
    print(result)