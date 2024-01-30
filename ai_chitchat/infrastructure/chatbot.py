import os
import requests

import openai


class ChatbotClient:
    def __init__(self, bot_type) -> None:
        self.model = None
        self.bot_type = bot_type

        # miiboで使用
        self.api_key = None
        self.agent_id = None

        self.setup()

    def setup(self):
        if self.bot_type == 'chatgpt':
            openai.api_key = os.environ.get('OPENAI_API_KEY')
            self.model = 'gpt-3.5-turbo'
        if self.bot_type == 'miibo':
            self.api_key = os.environ.get('MIIBO_API_KEY')
            self.agent_id = os.environ.get('MIIBO_AGENT_ID')

    def generate_response(self, message):
        '''APIから返ってきたレスポンス内のAIの返答のみを返す'''
        if self.bot_type == 'chatgpt':
            prompt = self._generate_prompt(message)
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=prompt,
                temperature=0.7
            )
            return response['choices'][0]['message']['content']
        if self.bot_type == 'miibo':
            url = 'https://api-mebo.dev/api'
            paylaod = self._generate_payload(message)
            headers = {'content-type': 'application/json'}
            response = requests.post(
                url=url,
                json=paylaod,
                headers=headers
            )
        return response.json()['bestResponse']['utterance']

    def _generate_prompt(self, message):
        '''APIに渡すプロンプトを生成する'''
        if self.bot_type == 'chatgpt':
            system_message = '''あなたは架空のAIキャラクターです。
            下記の箇条書きの条件を守ってユーザーの質問に答えてください。
            ・敬語を使わずフレンドリーな口調
            ・100文字以内'''
            return [
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': message}
            ]

    def _generate_payload(self, message):
        '''APIに渡すjson形式のデータを生成する'''
        if self.bot_type == 'miibo':
            return {
                'api_key': self.api_key,
                'agent_id': self.agent_id,
                'utterance': message
            }

def send_message_chatbot(user_text: str):
    '''チャットボットにメッセージを送信して返答テキストを取得する'''
    chatbot_client = ChatbotClient('miibo')
    return chatbot_client.generate_response(user_text)