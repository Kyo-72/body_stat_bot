from openai_api_caller import OpenaiApiCaller
from mock_openai_api_caller import MockOpenaiApiCaller

# モックするかどうか
IS_MOCKED = False

class OpenaiApiHandler:
    def __init__(self):
        # API Callerのインスタンスを作成
        self.api_caller = OpenaiApiCaller()
        self.mock_api_caller = MockOpenaiApiCaller()

    def create_request_body(self, content, system_content):
        # リクエストボディを作成
        return {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": content}
            ],
            "temperature": 0.7
        }

    def handle_request(self, content, system_content):
        request_body = self.create_request_body(content, system_content)
        
        # API呼び出しを行う
        if IS_MOCKED:
            response = self.mock_api_caller.send_request(request_body)
        else:
            response = self.api_caller.send_request(request_body)
        
        # レスポンスを返す
        return response
