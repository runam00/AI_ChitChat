import customtkinter as ct
from PIL import Image, ImageTk

from ..theme.strings import UIString
from ..theme.sizes import SidebarButtonSize
from ..theme.colors import BrandColor
from ..theme.images import BrandImage

class SidebarFrame(ct.CTkFrame):
    def __init__(self, root, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.root = root
        self._buttons: dict[str: ct.CTkButton] = {}
        self.current_mainframe_name: str = self.root.get_current_mainframe_name()

        # トップボタン
        self.home_button = ct.CTkButton(
            self,
            text=UIString.TOP,
            width=SidebarButtonSize.WIDTH,
            height=SidebarButtonSize.HEIGHT,
            hover_color=BrandColor.GRAY,
            image=self.generate_icon(BrandImage.TOP_BUTTON),
            compound='top',
            command=lambda: self.button_callback(UIString.TOP)
        )
        self._buttons[UIString.TOP] = self.home_button
        self.home_button.grid(row=0, column=0, padx=10, pady=(20, 10), sticky='ew')

        # チャットボタン
        self.chat_button = ct.CTkButton(
            self,
            text=UIString.CHAT,
            width=SidebarButtonSize.WIDTH,
            height=SidebarButtonSize.HEIGHT,
            hover_color=BrandColor.GRAY,
            image=self.generate_icon(BrandImage.CHAT_BUTTON),
            compound='top',
            command=lambda: self.button_callback(UIString.CHAT)
        )
        self._buttons[UIString.CHAT] = self.chat_button
        self.chat_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        # ボタンの色を設定
        self.set_buttons_color(self.current_mainframe_name)


    def generate_icon(self, image_path: str):
        '''ボタンに設定するアイコン画像を出力する'''
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)


    def set_buttons_color(self, selected: str):
        '''ボタンの選択状態によって、ボタンの色を変える'''
        for button_text, button in self._buttons.items():
            # 選択状態にあるならグレー
            if selected == button_text:
                color = BrandColor.GRAY
            # 選択されていない場合は透明
            else:
                color = 'transparent'
            button.configure(fg_color=color)


    def button_callback(self, selected: str):
        # フレームの選択状態を更新する
        self.root.update_current_mainframe_name(selected)

        # ボタンの色を更新
        self.set_buttons_color(selected)

        # 画面遷移
        self.root.show_frame(selected)