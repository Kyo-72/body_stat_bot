import openai
from param_store import get_param

class OpenaiApiCaller:
    def __init__(self):
        pass

    def send_request(self, request_body):
        # APIキーを設定
        openai.api_key = get_param("OPENAI_API_KEY")

        completion = openai.ChatCompletion.create(**request_body)

        return completion
