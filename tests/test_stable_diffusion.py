import pytest
from PIL import Image
from ai_chitchat.infrastructure.stable_diffusion import SDAPIClient

@pytest.fixture
def sd_api_client():
    return SDAPIClient()

def test_generate_image_input_string_returns_image_instance(sd_api_client):
    '''str型の文字列を渡すと、Imageクラスのインスタンスを返す'''
    prompt = '黒髪, 茶色の瞳, 女性'
    response = sd_api_client.generate_image(prompt)
    print(f'出力：{response}')
    assert isinstance(response, Image.Image)