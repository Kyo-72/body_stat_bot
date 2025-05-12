from logic.message.text_generator import simple_text_generator
from repositories.api.openai_api_repository import OpenaiApiRepository
from logic.message.create_report import generate_weight_report

def create_simple_message(average_health_data_for_period):
    message = simple_text_generator(average_health_data_for_period)
    return message

def daily_average_to_text(data):
    if len(data) == 0:
        return ''

    lines = []
    for dt, values in sorted(data.items()):
        date_str = dt.strftime("%Y-%m-%d")  # 日付だけに整形
        weight = values.get("avr_weight", "N/A")
        bfp = values.get("avr_bfp", "N/A")
        lines.append(f"{date_str}: avr_weight = {weight:.1f} kg, avr_bfp = {bfp:.1f} %")
    return "\n".join(lines)

def weekly_average_to_simple_text(data):
    if len(data) == 0:
        return ''
    # 各キーと値を文字列にして1行でまとめる
    text = f"start_date: {data['start_date']}, end_date: {data['end_date']}, avr_weight: {data['avr_weight']}, avr_bfp: {data['avr_bfp']}"
    return text

def both_weekly_average_to_text(this_week_data, last_week_data) -> str:
    this = weekly_average_to_simple_text(this_week_data)
    last = weekly_average_to_simple_text(last_week_data)
    return f"[This Week]\n{this}\n\n[Last Week]\n{last}"



def create_message(
        average_daily_data_this_week,
        average_daily_data_last_week,
        average_weekly_data_this_week,
        average_weekly_data_last_week
        ):
    # 非生成AIレポート作成
    report = generate_weight_report(average_weekly_data_this_week, average_weekly_data_last_week)
    # 生成AIに渡す用のデータ
    merged_for_daily_average = {**average_daily_data_this_week, **average_daily_data_last_week}
    daily_average_text = daily_average_to_text(merged_for_daily_average)
    weekly_average_text = both_weekly_average_to_text(
        average_weekly_data_this_week,
        average_weekly_data_last_week
    )

    body = '日毎の平均データはここです'
    body += daily_average_text
    body += '週ごとの平均データはここです'
    body += weekly_average_text
    system_content = """あなたは厳格な体重管理トレーナーです。  
以下に渡される2週間分の体重・体脂肪率の測定データと、各週の平均値をもとに、最新の週についてフィードバックしてください。
データが足りていない場合でも、渡されたデータを分析し可能な限り詳細にフィードバックを行ってください
- 今週の平均値が先週よりも増加している場合は、厳しく指導してください。
- 減少している場合は控えめに褒めてください。油断しないよう釘を刺す表現も入れてください。
- 停滞（増減がほぼない場合）も、サボっている可能性があるとして厳しく指摘してください。
- 特定の日に数値が明らかに増加している場合は、その日を名指しで指摘してください。
- 体重と体脂肪率の両方に対してそれぞれ触れてください。
"""


    open_api_repository = OpenaiApiRepository()
    response = open_api_repository.handle_request(body, system_content)
    message = report + response["choices"][0]["message"]["content"]
    print(message)

    return message



