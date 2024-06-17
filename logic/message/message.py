from logic.message.text_generator import simple_text_generator

def create_message(average_health_data_for_period):
    message = simple_text_generator(average_health_data_for_period)
    return message


