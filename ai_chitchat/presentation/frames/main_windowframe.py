import customtkinter as ct

from .sidebar_frame import SidebarFrame
from ..theme.colors import BrandColor
from ..theme.strings import UIString
from ..states.button_state import ButtonState
from .frame_mappings import FrameMapping

class MainWindowFrame(ct.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 初期値はトップページ
        self.button_state = ButtonState(UIString.TOP)

        self.frames = {}
        for v in UIString.get_values():
            frame_class = FrameMapping.get(v)
            if frame_class:
                frame = frame_class()
                self.frames[v] = frame
                frame.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')

        # 全体のレイアウトを設定
        # サイドバー用
        self.sidebar_frame = ct.CTkFrame(master=self, width=100)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        # メインフレーム用
        self.mainframe = ct.CTkFrame(master=self)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

        # サイドバーを表示
        self.sidebar_view = SidebarFrame(master=self.sidebar_frame, fg_color=BrandColor.DARK_GRAY)
        self.sidebar_view.pack(
            
        )

        # 最初にトップページを表示
        self.mainframe = self.show_mainframe(self.button_state)


    def show_mainframe(self, selected: str):
        '''フレームを表示する'''
        self.mainframe = self.frames[selected]
        self.mainframe.tkraise(self)