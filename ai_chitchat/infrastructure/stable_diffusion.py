import requests
import io
import base64
from PIL import Image

class SDAPIClient:
    BASE_URL = 'http://127.0.0.1:7860'
    DEFAULT_MODEL = 'realcartoonRealistic_v13.safetensors'

    def __init__(self):
        self.response = None
        self.models = []

        models_json = self._fetch_models()
        self._add_models(models_json)

        self.change_model(SDAPIClient.DEFAULT_MODEL)

    def generate_image(self, prompt):
        payload = {
            'prompt': prompt,
            'steps': 20
        }
        response = requests.post(url=f'{SDAPIClient.BASE_URL}/sdapi/v1/txt2img', json=payload)
        self.response = response.json()
        return Image.open(io.BytesIO(base64.b64decode(self.response['images'][0])))

    def change_model(self, model):
        model_hash_pairs = self._find_model(model)
        option_payload = {
            "sd_model_checkpoint": model_hash_pairs
        }
        return requests.post(url=f'{SDAPIClient.BASE_URL}/sdapi/v1/options', json=option_payload)

    def _fetch_models(self):
        return requests.get(f'{SDAPIClient.BASE_URL}/sdapi/v1/sd-models').json()

    def _add_models(self, models_json):
        for model in models_json:
            self.models.append(model['title'])

    def _find_model(self, model):
        for model_hash_pairs in self.models:
            if model in model_hash_pairs:
                return model_hash_pairs
            return