import customtkinter as ct

from ..theme.strings import UIString

class TopPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # アプリタイトル
        self.label = ct.CTkLabel(self, text=UIString.TITLE)
        self.label.pack()