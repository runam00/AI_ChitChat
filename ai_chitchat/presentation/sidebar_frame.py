import customtkinter as ct
import tkinter as tk
from PIL import Image, ImageTk

class SidebarFrame(ct.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # TODO 文言の文字列
        # トップボタン
        top_icon = Image.open('assets/images/house.png')
        top_icon = ImageTk.PhotoImage(top_icon)
        self.button_home = ct.CTkButton(
            self,
            text='TOP',
            width=60,
            height=60,
            image=top_icon,
            compound='top'
        )
        self.button_home.grid(row=0, column=0, padx=10, pady=(20, 10), sticky='ew')
        # チャットボタン
        chat_icon = Image.open('assets/images/chat-dots.png')
        chat_icon = ImageTk.PhotoImage(chat_icon)
        self.button_chat = ct.CTkButton(
            self,
            text='CHAT',
            width=60,
            height=60,
            fg_color='#393E46',
            hover_color='#393E46',
            image=chat_icon,
            compound='top'
        )
        self.button_chat.grid(row=1, column=0, padx=10, pady=10, sticky='ew')