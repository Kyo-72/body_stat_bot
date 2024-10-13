class OpenaiApiCallerStub:
    def __init__(self):
        pass

    def send_request(self, request_body):
        # モックのレスポンスとして、APIを呼び出さずにデータを返す
        return {
            "id": "chatcmpl-AFVgpaSdQiPbcQijt6n4VE2akTvMe",
            "object": "chat.completion",
            "created": 1728260099,
            "model": "gpt-3.5-turbo-0125",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "了解しました。API疎通テストが成功しました(モック)。",
                        "refusal": None
                    },
                    "logprobs": None,
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 37,
                "completion_tokens": 17,
                "total_tokens": 54,
                "prompt_tokens_details": {
                    "cached_tokens": 0
                },
                "completion_tokens_details": {
                    "reasoning_tokens": 0
                }
            },
            "system_fingerprint": None
        }
