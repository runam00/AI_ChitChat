import customtkinter as ct

from .frames.main_window_frame import MainWindowFrame
from .states.button_state import ButtonState
from .theme.strings import UIString

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.init_states()
        self.build_ui()


    def build_ui(self):
        self.title('AI_ChitChat')
        self.geometry('1200x600')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # メインフレーム
        self.main_frame = MainWindowFrame(master=self)
        self.main_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')


    def init_states(self):
        self._button_state = ButtonState(UIString.TOP)


    def get_button_state(self):
        return self._button_state