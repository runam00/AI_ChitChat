import customtkinter as ct
from PIL import Image

from ..theme.colors import BrandColor
from ..theme.images import BrandImagePath
from ..theme.sizes import ChatPageSize
from ..theme.fonts import ChatFrameFont
from ..theme.strings import UIString

class ChatPageFrame(ct.CTkFrame):
    def __init__(self, parent, root, **kwargs):
        super().__init__(parent, **kwargs)

        self.root = root

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.interface_frame = InterfaceFrame(self, width=600, height=600, fg_color='transparent')
        self.chat_history_frame = ChatHistoryFrame(self, self.root, width=600)
        self.interface_frame.grid(row=0, column=0)
        self.chat_history_frame.grid(row=0, column=1)


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



class ChatHistoryFrame(ct.CTkScrollableFrame):
    '''チャット履歴を表示するフレーム'''
    def __init__(self, parent, root, **kwargs):
        super().__init__(parent, **kwargs)

        self.root = root
        self._ai_icon = None
        self._messages_list = []
        self._message_count = 0

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # ユーザーアイコン
        self._user_icon = ct.CTkImage(
            Image.open(BrandImagePath.USER_ICON),
            size=ChatPageSize.IMAGE_ICON_SIZE
        )

        self.fetch_generated_image()
        self.fetch_messages_list()


    def fetch_generated_image(self):
        '''生成された画像を取得し、CTkImageクラスに格納する'''
        generated_image = self.root.get_generated_image()
        self._ai_icon = ct.CTkImage(generated_image, size=(ChatPageSize.IMAGE_ICON_SIZE))


    def fetch_messages_list(self):
        '''メッセージリストを取得する'''
        self._messages_list = self.root.get_messages_list()


    def place_message(self, message: dict, row: int):
        '''一つのメッセージを配置する'''
        # アイコン
        icon = ct.CTkButton(
            self,
            width=25,
            height=25,
            fg_color='transparent',
            border_color=BrandColor.BLUE,
            hover=False
        )

        # チャットメッセージ
        message_text = ct.CTkLabel(
            self,
            corner_radius=0,
            text=message['content'],
            text_color=BrandColor.WHITE
        )

        if message['role'] == 'AI':
            icon.configure(image=self._ai_icon)
            message_text.configure(fg_color=BrandColor.LIGHT_GRAY)
        elif message['role'] == 'user':
            icon.configure(image=self._user_icon)
            message_text.configure(fg_color=BrandColor.DARK_GRAY)

        icon.grid(row=row, column=0, padx=10, pady=(5, 0))
        message_text.grid(row=row, column=1, padx=10, pady=5)


    def place_all_messages(self):
        '''全てのメッセージを配置する'''
        for i, message in enumerate(self._messages_list):
            self.place_message(message, i)


    def add_message(self):
        self.fetch_generated_image()
        image = ct.CTkImage(self._ai_icon, size=(ChatPageSize.IMAGE_ICON_SIZE))
        icon = ct.CTkButton(self, image=image)
        # icon.grid(row=)