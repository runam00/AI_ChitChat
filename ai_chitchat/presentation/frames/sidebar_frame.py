import customtkinter as ct
from PIL import Image, ImageTk

from ..callbacks.button_callback import sidebar_button_callback

from ..theme.strings import UIString
from ..theme.sizes import SidebarButton
from ..theme.colors import BrandColor
from ..theme.images import BrandImage

class SidebarFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # トップボタン
        top_icon = Image.open(BrandImage.TOP_BUTTON)
        top_icon = ImageTk.PhotoImage(top_icon)
        self.button_home = ct.CTkButton(
            self,
            text=UIString.TOP,
            width=SidebarButton.WIDTH,
            height=SidebarButton.HEIGHT,
            fg_color='transparent',
            hover_color=BrandColor.GRAY,
            image=top_icon,
            compound='top',
            command=lambda: sidebar_button_callback(parent, UIString.TOP)
        )
        self.button_home.grid(row=0, column=0, padx=10, pady=(20, 10), sticky='ew')

        # チャットボタン
        chat_icon = Image.open(BrandImage.CHAT_BUTTON)
        chat_icon = ImageTk.PhotoImage(chat_icon)
        self.button_chat = ct.CTkButton(
            self,
            text=UIString.CHAT,
            width=SidebarButton.WIDTH,
            height=SidebarButton.HEIGHT,
            fg_color='transparent',
            hover_color=BrandColor.GRAY,
            image=chat_icon,
            compound='top',
        )
        self.button_chat.grid(row=1, column=0, padx=10, pady=10, sticky='ew')