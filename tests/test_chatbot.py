import pytest
from ai_chitchat.infrastructure.chatbot import ChatbotClient

@pytest.fixture
def gpt_chatbot_client():
    return ChatbotClient(bot_type='chatgpt')

@pytest.fixture
def miibo_chatbot_client():
    return ChatbotClient(bot_type='miibo')


def test_gpt_generate_response_prompt_return_response_str(gpt_chatbot_client):
    '''ChatGPTのAPIに質問文を渡すと、それに対する回答がstr型で返ってくる'''
    response_text = gpt_chatbot_client.generate_response('良い天気ですね')
    print(f'返答：{response_text}')
    assert isinstance(response_text, str)


def test_miibo_generate_response_return_response_str(miibo_chatbot_client):
    '''miiboのAPIに質問文を渡すと、それに対する回答がstr型で帰ってくる'''
    response_text = miibo_chatbot_client.generate_response('今日の調子はどうですか？')
    print(f'返答：{response_text}')
    assert isinstance(response_text, str)