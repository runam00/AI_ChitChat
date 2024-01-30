import requests
import json

class VVAPIClient:
    BASE_URL = 'http://127.0.0.1:50021'

    def generate_audio(self, text, speaker=2):
        query_data = self._post_audio_query(text, speaker)
        audio_data = self._post_synthesis(speaker, query_data)
        return audio_data

    def _post_audio_query(self, text, speaker):
        params = {
            'text': text,
            'speaker': speaker
        }
        response = requests.post(
            url=f'{VVAPIClient.BASE_URL}/audio_query',
            params=params
        )
        return response.json()

    def _post_synthesis(self, speaker, query_data):
        headers = {"Content-Type": "application/json"}
        params = {'speaker': speaker}
        response = requests.post(
            url=f'{VVAPIClient.BASE_URL}/synthesis',
            headers=headers,
            params=params,
            data=json.dumps(query_data)
        )
        return response.content