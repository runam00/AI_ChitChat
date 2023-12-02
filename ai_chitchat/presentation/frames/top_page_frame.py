import customtkinter as ct

from ..theme.strings import UIString

class TopPageFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # アプリタイトル
        self.label = ct.CTkLabel(self, text=UIString.TITLE)