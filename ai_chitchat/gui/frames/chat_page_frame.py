import customtkinter as ct
from PIL import Image

from ..theme.colors import BrandColor
from ..theme.images import BrandImagePath
from ..theme.sizes import ChatPageSize
from ..theme.fonts import ChatFrameFont
from ..theme.strings import UIString

class ChatPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.interface_frame = InterfaceFrame(self, width=600, height=600, fg_color='transparent')
        self.interface_frame.grid(row=0, column=0)


class InterfaceFrame(ct.CTkFrame):
    '''テキスト送信、音量調整、ダウンロードなどのユーザーインターフェースを配置するフレーム'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # ミュートトグルボタン
        self.mute_toggle_button = ct.CTkButton(
            self,
            width=ChatPageSize.BUTTON_WIDTH,
            height=ChatPageSize.BUTTON_HEIGHT,
            hover_color=BrandColor.GRAY,
            text=None
        )
        self.mute_toggle_button.grid(row=1, column=0, padx=(10, 5))

        # 音量調整ボタン
        self.audio_volume_slider = ct.CTkSlider(
            self,
            width=100,
            fg_color=BrandColor.DARK_GRAY,
            progress_color=BrandColor.WHITE,
            button_color=BrandColor.WHITE,
            hover=False
        )
        self.audio_volume_slider.grid(row=1, column=1)

        # 位置調整用のスペース
        space = ct.CTkFrame(self, width=250, height=20, fg_color=BrandColor.GRAY)
        space.grid(row=1, column=2)

        # 動画のリプレイボタン
        replay_button_icon = ct.CTkImage(Image.open(BrandImagePath.REPLAY_BUTTON), size=(25, 25))
        self.replay_button = ct.CTkButton(
            self,
            width=ChatPageSize.BUTTON_WIDTH,
            height=ChatPageSize.BUTTON_HEIGHT,
            fg_color='transparent',
            hover_color=BrandColor.GRAY,
            anchor='center',
            text=None,
            image=replay_button_icon
        )
        self.replay_button.grid(row=1, column=3)

        # ダウンロードボタン
        download_button_icon = ct.CTkImage(Image.open(BrandImagePath.DOWNLOAD_BUTTON), size=(25, 25))
        self.download_button = ct.CTkButton(
            self,
            width=ChatPageSize.BUTTON_WIDTH,
            height=ChatPageSize.BUTTON_HEIGHT,
            fg_color='transparent',
            hover_color=BrandColor.GRAY,
            anchor='center',
            text=None,
            image=download_button_icon,
        )
        self.download_button.grid(row=1, column=4)

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
        self.user_input_text_box.grid(row=2, column=0, columnspan=4, padx=(10, 0), pady=10)

        # 送信ボタン
        submit_button_icon = ct.CTkImage(Image.open(BrandImagePath.SUBMIT_BUTTON), size=(30, 30))
        submit_button = ct.CTkButton(
            self,
            width=50,
            height=50,
            fg_color='transparent',
            hover=False,
            text=None,
            image=submit_button_icon)
        submit_button.grid(row=2, column=4, padx=0)



class ChatHistoryFrame(ct.CTkFrame):
    '''チャット履歴を表示するフレーム'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)