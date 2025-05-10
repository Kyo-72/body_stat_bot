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

def create_message(average_data_this_week, average_data_last_week):
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
    report = generate_weight_report(average_data_this_week, average_data_last_week)
    # データをテキストにキャスト
    health_text = dict_to_simple_text(average_data_this_week, average_data_last_week)
    body = 'データはここです'
    body = body + health_text
    system_content = """あなたは厳格な体重管理トレーナーです。  
以下に渡される2週間分の体重・体脂肪率の測定データと、各週の平均値をもとに、最新の週についてフィードバックしてください。
- 今週の平均値が先週よりも増加している場合は、厳しく指導してください。
- 減少している場合は控えめに褒めてください。油断しないよう釘を刺す表現も入れてください。
- 停滞（増減がほぼない場合）も、サボっている可能性があるとして厳しく指摘してください。
- 特定の日に数値が明らかに増加している場合は、その日を名指しで指摘してください。
- 体重と体脂肪率の両方に対してそれぞれ触れてください。
- 文章は100〜200文字以内に収めてください。
"""


    open_api_repository = OpenaiApiRepository()
    response = open_api_repository.handle_request(body, system_content)
    message = report + response["choices"][0]["message"]["content"]
    print(message)

    return message



