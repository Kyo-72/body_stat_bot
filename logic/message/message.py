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
以下に渡される 2 週間分の体重・体脂肪率の測定データと各週の平均値をもとに、最新の週についてのみ フィードバックを作成してください。

【判定ルール】  
・ 今週平均が先週より増加 → 厳しく指導  
・ 今週平均が減少 → 控えめに褒めつつ油断を戒める  
・ 増減がほぼない → サボっている可能性を厳しく指摘  
・ 特定の日に数値が大きく増加している場合は、その日付を名指しで指摘  
・ 体重と体脂肪率の両方に必ず触れる  

【出力フォーマット】  
・ メッセージは フィードバック本文のみ。平均値などの数値の再掲は不要   
- 本文は 500 文字以内。
- 数字を表示する際や強調の場合は *太字* の形で 先頭と末尾を半角アスタリスク1個で囲い前後に半角スペースを入れる


【ボリューム指示】  
以下の観点でデータを分析してください
1. 今週の体重トレンド  
2. 今週の体脂肪率トレンド  
3. 特定日の急増・急減があれば名指し指摘    
4. 具体的な改善策（例:夜食禁止、HIIT 20 分追加 等）  
5. 次週への厳命・目標設定  
6. 今後へのコメント  
"""

    open_api_repository = OpenaiApiRepository()
    response = open_api_repository.handle_request(body, system_content)
    message = report + '\n'+ response["choices"][0]["message"]["content"]
    print(message)

    return message



