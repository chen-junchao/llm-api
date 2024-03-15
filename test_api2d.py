import unittest

from api2d import API2D

class TestAPI2D(unittest.TestCase):
    def test_chat_completions(self):
        FORWARD_KEY = 'fkxxxxx' # <-- your forward key
        api = API2D()
        api.init_forward_key(FORWARD_KEY)
        content = "讲个短笑话"
        response = api.chat_completions(messages=[{
                   "role": "user",
                   "content": content
               }])
        res_json = response.json()
        print(res_json['choices'][0]['message']['content'])
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
