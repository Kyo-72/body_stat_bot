def generate_weight_report(this_week_data, last_week_data):

    weight_diff_text = 'xxx'
    body_fat_diff_text = 'xxx'
    # 先週、今週分のデータが揃っていれば差分を計算する
    if not (len(this_week_data) == 0) and not( len(last_week_data) == 0):
        weight_diff_text, body_fat_diff_text = __generate_diff_text(this_week_data, last_week_data)
    # レポートテキスト生成
    report = f"""
*今週の体重と体脂肪率レポート*

*今週のデータ:*
- 体重: {this_week_data['avr_weight']} kg
-体脂肪率: {this_week_data['avr_bfp']}%

*先週と比較した増減:*
 - 体重: {weight_diff_text}
 - 体脂肪率: {body_fat_diff_text}
--
"""
    return report.strip()

def __generate_diff_text(this_week_data, last_week_data):
    weight_diff, body_fat_diff = __calc_diff(this_week_data, last_week_data)
    # 増減の符号に応じたフォーマット
    weight_diff_text = f"{weight_diff:+.1f} kg"
    body_fat_diff_text = f"{body_fat_diff:+.1f}%"

    return weight_diff_text, body_fat_diff_text

def __calc_diff(this_week_data, last_week_data):
    # 体重と体脂肪率の増減を計算
    weight_diff = this_week_data["avr_weight"] - last_week_data["avr_weight"]
    body_fat_diff = this_week_data["avr_bfp"] - last_week_data["avr_bfp"]

    return weight_diff, body_fat_diff


