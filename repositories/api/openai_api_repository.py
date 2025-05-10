from api.openai_api.openai_api_caller import OpenaiApiCaller
from api.openai_api.openai_api_caller_stub import OpenaiApiCallerStub

# スタブするかどうか
IS_STUBED = False

class OpenaiApiRepository:
    def __init__(self):
        # API Callerのインスタンスを作成
        self.api_caller = OpenaiApiCaller()
        self.mock_api_caller = OpenaiApiCallerStub()

    def handle_request(self, content, system_content='あなたはトレーナーです'):
        request_body = self.__create_request_body(content, system_content)
        
        # API呼び出しを行う
        if IS_STUBED:
            response = self.mock_api_caller.send_request(request_body)
        else:
            response = self.api_caller.send_request(request_body)
        
        # レスポンスを返す
        return response
    
    def __create_request_body(self, content, system_content):
        # リクエストボディを作成
        return {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": content}
            ],
            "temperature": 0.7
        }
