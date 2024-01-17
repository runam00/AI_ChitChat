from PIL import Image, ImageTk
import threading as th

import cv2
import tkinter as tk
import customtkinter as ct

from ..theme.colors import BrandColor


lock = th.Lock()

class VideoPlayer(ct.CTkFrame):
    def __init__(self, parent, width, height, image, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)

        self.width = width
        self.height = height

        self.video = None
        self.playing = False

        self.pack(expand=True, fill=tk.BOTH)

        image = ct.CTkImage(image, size=(self.width, self.height))

        # 動画をクリックすると再生が可能になる
        self.start_button = ct.CTkButton(
            self,
            width=self.width,
            height=self.height,
            fg_color=BrandColor.DARK_GRAY,
            hover=False,
            text=None,
            anchor='center',
            image=image,
            command=self.start
        )
        self.start_button.pack()

    def load(self, path):
        '''ビデオを読み込む'''
        self.video = cv2.VideoCapture(path)

    def start(self):
        if self.video is None:
            print('No video loaded')
            return

        self.playing = not self.playing

        if self.playing:
            thread = th.Thread(target=self.draw, daemon=True)
            thread.start()
        else:
            thread = None

    def draw(self):
        while self.playing:

            ret, frame = self.video.read()

            if not ret:
                self.playing = False
            else:
                self._set_frame(frame)

    def _set_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)
        # resized_image = self._scale_to_width(pil_image)
        image = ct.CTkImage(pil_image, size=(self.width, self.height))
        ###デバッグ
        print(type(image))

        self.start_button.configure(image=image)

    def _scale_to_width(self, image):
        '''アスペクト比を保ったまま横幅に合わせる'''
        width = self.width
        height = round(image.height * width / image.width)
        return image.resize((width, height))