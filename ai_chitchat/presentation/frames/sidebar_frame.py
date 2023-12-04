import customtkinter as ct
from PIL import Image, ImageTk

from ..callbacks.button_callback import sidebar_button_callback

from ..theme.strings import UIString
from ..theme.sizes import SidebarButton
from ..theme.colors import BrandColor
from ..theme.images import BrandImage

class SidebarFrame(ct.CTkFrame):
    def __init__(self, master, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.master = master
        self._buttons: dict[str: ct.CTkButton] = {}

        # # トップボタン
        top_icon = Image.open(BrandImage.TOP_BUTTON)
        top_icon = ImageTk.PhotoImage(top_icon)
        self.home_button = ct.CTkButton(
            self,
            text=UIString.TOP,
            width=SidebarButton.WIDTH,
            height=SidebarButton.HEIGHT,
            hover_color=BrandColor.GRAY,
            image=top_icon,
            compound='top',
        )
        self._buttons[UIString.TOP] = self.home_button
        self.home_button.configure(command=lambda: sidebar_button_callback(self, self.master, UIString.TOP))
        self.home_button.grid(row=0, column=0, padx=10, pady=(20, 10), sticky='ew')

        # チャットボタン
        chat_icon = Image.open(BrandImage.CHAT_BUTTON)
        chat_icon = ImageTk.PhotoImage(chat_icon)
        self.chat_button = ct.CTkButton(
            self,
            text=UIString.CHAT,
            width=SidebarButton.WIDTH,
            height=SidebarButton.HEIGHT,
            hover_color=BrandColor.GRAY,
            image=chat_icon,
            compound='top',
        )
        self._buttons[UIString.CHAT] = self.chat_button
        self.chat_button.configure(command=lambda: sidebar_button_callback(self, self.master, UIString.CHAT))
        self.chat_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        # ボタンの色を設定
        self.set_buttons_color()


    def set_buttons_color(self):
        '''ボタンの選択状態によって、ボタンの色を変える'''
        self.button_state = self.master.get_button_state()
        selected = self.button_state.selected()
        for button_text, button in self._buttons.items():
            # 選択状態にあるならグレー
            if selected == button_text:
                color = BrandColor.GRAY
            # 選択されていない場合は透明
            else:
                color = 'transparent'
            button.configure(fg_color=color)