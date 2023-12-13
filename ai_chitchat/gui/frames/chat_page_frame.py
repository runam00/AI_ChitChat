import customtkinter as ct
from PIL import Image

from ..theme.colors import BrandColor
from ..theme.images import BrandImagePath
from ..theme.sizes import ChatPageSize

class ChatPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.interface_frame = InterfaceFrame(self, fg_color=BrandColor.GRAY)
        self.interface_frame.grid(row=0, column=0)


class InterfaceFrame(ct.CTkFrame):
    '''テキスト送信、音量調整、ダウンロードなどのユーザーインターフェースを配置するフレーム'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
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
        self.mute_toggle_button.grid(row=1, column=0)

        # 音量調整ボタン
        self.audio_volume_slider = ct.CTkSlider(
            self,
            width=80,
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


class ChatHistoryFrame(ct.CTkFrame):
    '''チャット履歴を表示するフレーム'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)