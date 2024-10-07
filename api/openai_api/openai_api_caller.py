import openai
import os

class OpenaiApiCaller:
    def __init__(self):
        pass

    def send_request(self, request_body):
        # APIキーを設定
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        completion = openai.ChatCompletion.create(**request_body)

        return completion
