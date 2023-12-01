import customtkinter as ct

from .frames.main_windowframe import MainWindowFrame

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title('AI_ChitChat')
        self.geometry('1200x600')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # メインフレーム
        self.main_frame = MainWindowFrame(master=self)
        self.main_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
