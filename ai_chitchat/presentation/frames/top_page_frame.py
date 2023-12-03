import customtkinter as ct

from ..theme.strings import UIString

class TopPageFrame(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # アプリタイトル
        self.label = ct.CTkLabel(self, text=UIString.TITLE)