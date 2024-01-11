import openai
import os


class ChatbotClient:
    def __init__(self, bot_type) -> None:
        self.model = None
        self.bot_type = bot_type

        self.setup_chatgpt()


    def setup_chatgpt(self):
        if self.bot_type == 'chatgpt':
            openai.api_key = os.environ.get('OPENAI_API_KEY')
            self.model = 'gpt-3.5-turbo'


    def generate_response(self, message):
        '''APIからのレスポンスを返す'''
        prompt = self.generate_prompt(message)

        if self.bot_type == 'chatgpt':
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=prompt,
                temperature=0.7
            )
            return response['choices'][0]['message']['content']
        return

    def generate_prompt(self, message):
        '''APIに渡すプロンプトを生成する'''
        system_message = '''あなたはフレンドリーな口調でユーザーの質問に答えてください。'''
        return [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': message}
        ]