from logic.message.text_generator import simple_text_generator
from repositories.api.openai_api_repository import OpenaiApiRepository
from logic.message.create_report import generate_weight_report

def create_simple_message(average_health_data_for_period):
    message = simple_text_generator(average_health_data_for_period)
    return message

def dict_to_simple_text(data):
    # 各キーと値を文字列にして1行でまとめる
    text = f"start_date: {data['start_date']}, end_date: {data['end_date']}, avr_weight: {data['avr_weight']}, avr_bfp: {data['avr_bfp']}"
    return text

def create_message(average_health_data_for_period):
    # レポート作成
    # サンプルデータ
    this_week = {
        "avr_weight": 68.5,
        "avr_bfp": 23.8
    }

    last_week = {
        "avr_weight": 69.0,
        "avr_bfp": 24.2
    }
    report = generate_weight_report(this_week, last_week)
    # データをテキストにキャスト
    health_text = dict_to_simple_text(average_health_data_for_period)
    body = 'データはここです'
    body = body + health_text
    system_content = "あなたは厳しい体重管理トレーナーです。ユーザーの体重や体脂肪率が減少していない場合、厳しく注意してください。減少している場合は控えめに褒めてください。過去3週間のデータを基に最新の週のフィードバックを行い、進捗またはその欠如について言及してください。常に厳しい口調で、タメ口で指導してください。日本語で出力すべきですが、アメリカンジョークも交えてください"

    open_api_repository = OpenaiApiRepository()
    response = open_api_repository.handle_request(body, system_content)
    message = report + response["choices"][0]["message"]["content"]
    print(message)

    return message



