import textwrap

def simple_text_generator(wealth_data_for_preriod: dict):
    formatted_start_date = wealth_data_for_preriod['start_date'].strftime('%Y年%m月%d日');
    formatted_end_date = wealth_data_for_preriod['end_date'].strftime('%Y年%m月%d日');

    res_text = f'''
                    {formatted_start_date}から{formatted_end_date}までの平均体重/平均体脂肪率
                    平均体重  : {wealth_data_for_preriod['avr_weight']}
                    平均体脂肪率 : {wealth_data_for_preriod['avr_bfp']}
                '''
    
    # インデントを取り除く
    res_text = textwrap.dedent(res_text).strip()
    
    return res_text