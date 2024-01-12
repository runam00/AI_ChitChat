import pytest
from ai_chitchat.infrastructure.chatbot import ChatbotClient

@pytest.fixture
def gpt_chatbot_client():
    return ChatbotClient(bot_type='chatgpt')


def test_gpt_generate_response_prompt_return_response_str(gpt_chatbot_client):
    '''チャットボットのAPIに質問文を渡すと、それに対する回答がstr型で返ってくる'''
    response_text = gpt_chatbot_client.generate_response('良い天気ですね')
    print(f'返答：{response_text}')
    assert isinstance(response_text, str)