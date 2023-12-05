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
        
        self.__current_mainframe: str = None  # 現在表示しているメインフレームの名前
        self.__mainframes: dict[str: ct.CTkFrame] = {}  # 画面遷移で使用するためのメインフレーム

        # UIを表示
        self.build_ui()
        # 起動時にトップページを表示
        self.show_frame(UIString.TOP)


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
        self.mainframe_area.columnconfigure(0, weight=1)
        self.mainframe_area.rowconfigure(0, weight=1)

        # サイドバーのフレームを設置
        self.sidebar_frame = SidebarFrame(
            master=self,
            parent=self.sidebar_area,
            fg_color=BrandColor.DARK_GRAY,
            corner_radius=0
        )
        self.sidebar_frame.pack(expand=True, fill=tk.BOTH, padx=0, pady=0)

        # メインフレームを生成
        self.mainframes = {
            # トップページのメインフレーム
            UIString.TOP: TopPageFrame(
                parent=self.mainframe_area,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            ), 
            # チャットページのメインフレーム
            UIString.CHAT: ChatPageFrame(
                parent=self.mainframe_area,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            )
        }
        # メインフレームを全て設置する
        for frame in self.mainframes.values():
            frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')


    def show_frame(self, frame_name: str):
        frame = self.mainframes[frame_name]
        frame.tkraise()


    @property
    def current_mainframe(self):
        return self.__current_mainframe


    @current_mainframe.setter
    def current_mainframe(self, current_mainframe):
        self.__current_mainframe = current_mainframe


    @property
    def mainframes(self):
        return self.__mainframes


    @mainframes.setter
    def mainframes(self, mainframes):
        self.__mainframes = mainframes