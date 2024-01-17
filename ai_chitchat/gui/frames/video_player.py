from PIL import Image, ImageTk
import threading as th
import pyaudio
import wave

import cv2
import tkinter as tk
import customtkinter as ct

from ..theme.colors import BrandColor

class VideoPlayer(ct.CTkFrame):
    def __init__(self, parent, width, height, image, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)

        self.width = width
        self.height = height

        self.video = None
        self.audio = None

        self.pack(expand=True, fill=tk.BOTH)

        # 最初に生成された画像を表示
        image = image.resize((self.width, self.height))
        image = ImageTk.PhotoImage(image)

        # 動画をクリックすると再生が可能になる
        self.start_button = tk.Button(
            self,
            width=self.width,
            height=self.height,
            bg=BrandColor.DARK_GRAY,
            image=image,
            command=self.start
        )
        self.start_button.image = image
        self.start_button.pack()

    def load(self, video, audio):
        '''ビデオと音声ファイルを読み込む'''
        self.video = video
        self.audio = audio

    def start(self):
        # 再生ボタンをクリック不可にする
        self.start_button.configure(state='disabled')

        if self.video is None:
            print('No video loaded')
            return

        thread_video = th.Thread(target=self.play_video, daemon=True)
        thread_audio = th.Thread(target=self.play_audio, daemon=True)

        thread_video.start()
        thread_audio.start()

        # 再生ボタンを再度クリック可能にする
        self.start_button.configure(state='normal')

    def play_video(self):
        self.cap = cv2.VideoCapture(self.video)
        # 動画を最初に巻き戻す
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # フレームレートを取得
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        print(f'fps：{fps}')
        # フレーム数を取得
        frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(f'フレーム数：{frame_count}')

        # フレーム間の待機時間を設定（fpsに基づく）
        delay = int(600 / fps)
        print(delay)

        # 再生
        while True:
            ret, frame = self.cap.read()

            # 再生できるフレームが無くなったら動画を終了する
            if not ret:
                self.cap.release()
                break

            self._set_frame(frame)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

    def _set_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)
        resized_image = self._scale_to_width(pil_image)
        image = ImageTk.PhotoImage(resized_image)
        self.start_button.config(image=image)
        self.start_button.image = image

    def _scale_to_width(self, image):
        '''アスペクト比を保ったまま横幅に合わせる'''
        width = self.width
        height = round(image.height * width / image.width)
        return image.resize((width, height))

    def play_audio(self):
        self.wav = wave.open(self.audio, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(self.wav.getsampwidth()),
            channels=self.wav.getnchannels(),
            rate=self.wav.getframerate(),
            output=True
        )

        chunk = 1024
        data = self.wav.readframes(chunk)

        while data:
            stream.write(data)
            data = self.wav.readframes(chunk)

        stream.stop_stream()
        stream.close()

        p.terminate()
        self.wav.close()