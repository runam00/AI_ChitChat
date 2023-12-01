import customtkinter as ct

class TopMainFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # アプリタイトル
        self.label = ct.CTkLabel(self, text='chat frame')