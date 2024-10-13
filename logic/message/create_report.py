def generate_weight_report(this_week_data, last_week_data):

    # 体重と体脂肪率の増減を計算
    weight_diff = this_week_data["avr_weight"] - last_week_data["avr_weight"]
    body_fat_diff = this_week_data["avr_bfp"] - last_week_data["avr_bfp"]

    # 増減の符号に応じたフォーマット
    weight_diff_text = f"{weight_diff:+.1f} kg"
    body_fat_diff_text = f"{body_fat_diff:+.1f}%"

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

