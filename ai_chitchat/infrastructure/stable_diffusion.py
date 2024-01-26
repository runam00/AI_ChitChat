import requests
import io
import base64
from PIL import Image

class SDAPIClient:
    BASE_URL = "http://127.0.0.1:7860"

    def __init__(self):
        self.response = None

    def generate_image(self, prompt):
        payload = {
            'prompt': prompt,
            'steps': 20
        }
        response = requests.post(url=f'{SDAPIClient.BASE_URL}/sdapi/v1/txt2img', json=payload)
        self.response = response.json()
        return Image.open(io.BytesIO(base64.b64decode(self.response['images'][0])))
