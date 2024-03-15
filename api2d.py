# coding=utf-8
# Author: oheck
# Date: 2024-3-15

import requests

class API2D:
    def __init__(self):
        self.url = "https://openai.api2d.net/v1/chat/completions"

    def chat_completions(self, model='gpt-3.5-turbo', messages=None, safe_mode=False, moderation=False, moderation_stop=False, stream=False, max_tokens=-1):
        if not self.forward_key:
            raise ValueError('Forward key not set')
        data = {
            'model': model,
            'messages': messages,
            'safe_mode': safe_mode,
        }
        if moderation:
            data['moderation'] = moderation
        if moderation_stop:
            data['moderation_stop'] = moderation_stop
        if stream:
            data['stream'] = stream
        if max_tokens > 0:
            data['max_tokens'] = max_tokens

        response = requests.post(self.url, headers=self.headers, json=data)
        return response

    def init_forward_key(self, forward_key):
        self.forward_key = forward_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.forward_key}'
        }
