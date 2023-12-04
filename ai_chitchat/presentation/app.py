import customtkinter as ct
import tkinter as tk

from .frames.top_page_frame import TopPageFrame
from .frames.chat_page_frame import ChatPageFrame
from .frames.sidebar_frame import SidebarFrame
from .states.button_state import ButtonState
from .theme.strings import UIString
from .theme.colors import BrandColor

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.init_states()
        self.build_ui()
        # 起動時にトップページを表示
        # self.change_mainframe(UIString.TOP)


    def build_ui(self):
        self.title('AI_ChitChat')
        self.geometry('1200x600')

        # 2×1でグリッドを設定
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # サイドバー設置用スペース
        self.sidebar_area = ct.CTkFrame(master=self, width=100, corner_radius=0)
        self.sidebar_area.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        # メインフレーム設置用スペース
        self.mainframe_area = ct.CTkFrame(master=self, corner_radius=0)
        self.mainframe_area.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')

        # サイドバーのフレームを設置
        self.sidebar_frame = SidebarFrame(
            master=self, 
            parent=self.sidebar_area, 
            fg_color=BrandColor.DARK_GRAY, 
            corner_radius=0
        )
        self.sidebar_frame.pack(expand=True, fill=tk.BOTH, padx=0, pady=0)

        # メインフレームを生成
        self._mainframes = {
            UIString.TOP: TopPageFrame(parent=self.mainframe_area), 
            UIString.CHAT: ChatPageFrame(parent=self.mainframe_area)
        }
        # メインフレームを全て設置する
        for frame in self._mainframes.values():
            frame.place()


    def init_states(self):
        self._button_state = ButtonState(selected=UIString.TOP)


    def get_button_state(self):
        return self._button_state


    def change_mainframe(self, frame_name: str):
        '''フレームを前面に表示する'''
        frame = self._mainframes[frame_name]
        frame.tkraise()