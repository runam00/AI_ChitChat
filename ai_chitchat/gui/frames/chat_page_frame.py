import customtkinter as ct
import tkinter as tk
from PIL import Image

from ..theme.colors import BrandColor
from ..theme.images import BrandImagePath
from ..theme.sizes import ChatPageSize
from ..theme.fonts import ChatFrameFont
from ..theme.strings import UIString
from .video_player import VideoPlayer
from lib.add_chat_message import add_chat_message
from lib.generate_audio import generate_audio
from lib.play_video import play_video
from lib.generate_video import generate_video


class ChatPageFrame(ct.CTkFrame):
    def __init__(self, parent, root, **kwargs):
        super().__init__(parent, **kwargs)

        self.root = root

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        image = self.root.get_generated_image()

        self.video_player = VideoPlayer(self, width=500, height=500, image=image)
        self.interface_frame = InterfaceFrame(self, root, fg_color='transparent')
        self.chat_history_frame = ChatHistoryFrame(self, self.root, width=900, fg_color='transparent')

        self.video_player.grid(row=0, column=0, padx=(80, 0), pady=(50, 10), sticky='s')
        self.interface_frame.grid(row=1, column=0, padx=(80, 0), pady=(10, 50), sticky='new')
        self.chat_history_frame.grid(row=0, column=1, rowspan=2, padx=(40, 80), pady=50, sticky='nse')

        self.interface_frame.submit_button.configure(command=self.on_submit_button_clicked)

    def on_submit_button_clicked(self):
        '''送信ボタンを押したときのコールバック関数'''
        # ボタンを使用不可にする
        self.interface_frame.submit_button.configure(state='disabled')
        # チャットメッセージを配置
        response_text = add_chat_message(self)
        # 音声を生成する
        generate_audio(self, response_text)
        # 動画を生成する
        generate_video(self)
        # 動画を再生する
        play_video(self)
        # ボタンを使用可能に戻す
        self.interface_frame.submit_button.configure(state='normal')

    def get_root(self):
        return self.root

    def get_interface_frame(self):
        return self.interface_frame

    def get_chat_history_frame(self):
        return self.chat_history_frame

    def get_video_player(self):
        return self.video_player


class InterfaceFrame(ct.CTkFrame):
    '''テキスト送信、音量調整、ダウンロードなどのユーザーインターフェースを配置するフレーム'''
    def __init__(self, parent, root, **kwargs):
        super().__init__(parent, **kwargs)

        self.root = root

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # # 音量調節アイコン
        # sound_icon_image = ct.CTkImage(Image.open(BrandImagePath.SOUND_ICON), size=(25, 25))
        # self.sound_icon = ct.CTkButton(
        #     self,
        #     width=ChatPageSize.BUTTON_WIDTH,
        #     height=ChatPageSize.BUTTON_HEIGHT,
        #     fg_color='transparent',
        #     hover_color=BrandColor.GRAY,
        #     text=None,
        #     image=sound_icon_image
        # )
        # self.sound_icon.grid(row=1, column=0)

        # # 音量調整スライダー
        # self.audio_volume_slider = ct.CTkSlider(
        #     self,
        #     width=100,
        #     fg_color=BrandColor.DARK_GRAY,
        #     progress_color=BrandColor.WHITE,
        #     button_color=BrandColor.WHITE,
        #     hover=False
        # )
        # self.audio_volume_slider.grid(row=1, column=1)

        # 位置調整用のスペース
        space = ct.CTkFrame(self, width=250, height=20, fg_color=BrandColor.GRAY)
        space.grid(row=1, column=2)

        # 動画のリプレイボタン
        # replay_button_icon = ct.CTkImage(Image.open(BrandImagePath.REPLAY_BUTTON), size=(25, 25))
        # self.replay_button = ct.CTkButton(
        #     self,
        #     width=ChatPageSize.BUTTON_WIDTH,
        #     height=ChatPageSize.BUTTON_HEIGHT,
        #     fg_color='transparent',
        #     hover_color=BrandColor.GRAY,
        #     anchor='center',
        #     text=None,
        #     image=replay_button_icon
        # )
        # self.replay_button.grid(row=1, column=3)

        # ダウンロードボタン
        # download_button_icon = ct.CTkImage(Image.open(BrandImagePath.DOWNLOAD_BUTTON), size=(25, 25))
        # self.download_button = ct.CTkButton(
        #     self,
        #     width=ChatPageSize.BUTTON_WIDTH,
        #     height=ChatPageSize.BUTTON_HEIGHT,
        #     fg_color='transparent',
        #     hover_color=BrandColor.GRAY,
        #     anchor='center',
        #     text=None,
        #     image=download_button_icon,
        # )
        # self.download_button.grid(row=1, column=4)

        # ユーザーの質問を入力&送信するテキストボックス
        self.user_input_text_box = ct.CTkEntry(
            self,
            width=ChatPageSize.TEXT_BOX_WIDTH,
            height=ChatPageSize.TEXT_BOX_HEIGHT,
            fg_color=BrandColor.WHITE,
            text_color=BrandColor.DARK_GRAY,
            placeholder_text=UIString.INPUT_HINT,
            placeholder_text_color=BrandColor.LIGHT_GRAY,
            font=ChatFrameFont.INPUT_TEXT
        )
        self.user_input_text_box.grid(row=2, column=0, columnspan=4, pady=10)

        # 送信ボタン
        submit_button_icon = ct.CTkImage(Image.open(BrandImagePath.SUBMIT_BUTTON), size=(30, 30))
        self.submit_button = ct.CTkButton(
            self,
            width=50,
            height=50,
            fg_color='transparent',
            hover=False,
            text=None,
            image=submit_button_icon,
        )
        self.submit_button.grid(row=2, column=4)

    def get_user_text(self):
        '''UIからユーザーが入力したテキストを取得'''
        return self.user_input_text_box.get()


class ChatHistoryFrame(ct.CTkScrollableFrame):
    '''チャット履歴を表示するフレーム'''
    def __init__(self, parent, root, **kwargs):
        super().__init__(parent, **kwargs)

        self.root = root
        self._ai_icon = None
        self._messages_list = []
        self._message_count = 0

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ユーザーアイコンを用意
        self._user_icon = ct.CTkImage(
            Image.open(BrandImagePath.USER_ICON),
            size=ChatPageSize.IMAGE_ICON_SIZE
        )

        self.fetch_generated_image()
        self.fetch_messages_list()
        self.place_all_messages()

    def fetch_generated_image(self):
        '''生成された画像を取得し、CTkImageクラスに格納する'''
        generated_image = self.root.get_generated_image()
        self._ai_icon = ct.CTkImage(generated_image, size=(ChatPageSize.IMAGE_ICON_SIZE))

    def fetch_messages_list(self):
        '''メッセージリストを取得する'''
        self._messages_list = self.root.get_messages_list()

    def place_message(self, message: dict, row: int):
        '''一つのメッセージを配置する'''

        if message['role'] == 'AI':
            icon_image = self._ai_icon
            bg = BrandColor.GRAY
        elif message['role'] == 'user':
            icon_image = self._user_icon
            bg = BrandColor.DARK_GRAY

        message_frame = ChatMessageFrame(self, icon_image, message['content'], fg_color=bg, corner_radius=0)
        message_frame.grid(row=row, column=0, padx=5, pady=(5, 0), sticky='nsew')

    def place_all_messages(self):
        '''全てのメッセージを配置する'''
        for i, message in enumerate(self._messages_list):
            self.place_message(message=message, row=i)


class ChatMessageFrame(ct.CTkFrame):
    def __init__(self, parent, icon, message, **kwargs):
        super().__init__(parent, **kwargs)
        self.icon_image = icon
        self.message = message

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # アイコン
        self._icon = ct.CTkButton(
            self,
            width=30,
            height=30,
            fg_color='transparent',
            command='top',
            anchor='center',
            hover=False,
            image=self.icon_image,
            text=None,
            state='disabled'
        )

        # チャットメッセージ
        self._message_text = tk.Message(
            self,
            width=500,
            pady=10,
            bg=self._fg_color,
            fg=BrandColor.WHITE,
            font=ChatFrameFont.MESSAGE_TEXT,
        )

        self.set_text()

        self._icon.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
        self._message_text.grid(row=0, column=1, padx=0, pady=0, sticky='w')

    def set_text(self):
        '''テキストを挿入する'''
        self._message_text.configure(text=self.message)