import customtkinter as ct

class ChatPageFrame(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # アプリタイトル
        self.label = ct.CTkLabel(self, text='chat frame')
        self.label.pack()