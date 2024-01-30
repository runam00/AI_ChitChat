from infrastructure.voicevox import VVAPIClient
from .file_utils import generate_filename

def generate_audio(frame, text):
    root = frame.get_root()

    # voicevoxのAPIを使用して音声生成
    vv_api_client = VVAPIClient()
    audio_data = vv_api_client.generate_audio(text, speaker=2)

    # results/audioフォルダに生成した画像を保存
    filename = generate_filename('audio', '.wav')
    audio_path = f'results/audio/{filename}'
    with open(audio_path, 'wb') as f:
        f.write(audio_data)

    # Appクラスで使われる音声のパスを更新
    root.set_generated_audio(audio_path)