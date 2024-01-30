import os

import customtkinter as ct
import tkinter as tk
from PIL import Image
from moviepy.editor import AudioFileClip

from lib.file_utils import read_txt_file, fetch_latest_file
from .frames.top_page_frame import TopPageFrame
from .frames.chat_page_frame import ChatPageFrame
from .frames.sidebar_frame import SidebarFrame
from .states.frame_state import FrameState
from .theme.strings import UIString
from .theme.colors import BrandColor

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self._temp_dir = None  # 一時フォルダのパス
        self._generated_image = None  # 生成された画像のパス
        self._generated_audio = None  # 生成された音声ファイルのパス
        self._generated_video = None  # 生成されたトーキングフォト動画のパス
        self._messages_list: list[dict[str: str]] = []  # チャットの履歴 {'role': '','content': ''}

        self._ai_chitchat_dir = os.getcwd()  # AI_ChitChatのパス
        self._webui_dir = None  #weubiが置いてあるディレクトリパス

        self._frame_state = FrameState()  # フレームに関する状態を管理する
        self._frame_state.current_mainframe = UIString.TOP  # 初期値はトップページ

        self._generated_image = 'assets/images/sample01.png'

        # アプリに必要なツールのパスを設定
        self.set_tool_path()

        # UIを表示
        self.build_ui()
        # 起動時にトップページを表示
        self.show_frame(UIString.TOP)
        # 指定したウィジェット以外の場所をクリックした際、フォーカスを外すためのイベントを設定
        self.bind('<Button-1>', self.remove_focus)

    def build_ui(self):

        self.title('AI_ChitChat')
        self.geometry('1440x810')
        self.minsize(1440, 810)
        ct.set_appearance_mode("dark")

        # 2×1でグリッドを設定
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # サイドバー設置用スペース
        self.sidebar_area = ct.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_area.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')
        # メインフレーム設置用スペース
        self.mainframe_area = ct.CTkFrame(self, corner_radius=0)
        self.mainframe_area.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')
        self.mainframe_area.columnconfigure(0, weight=1)
        self.mainframe_area.rowconfigure(0, weight=1)

        # サイドバーのフレームを設置
        self.sidebar_frame = SidebarFrame(
            root=self,
            parent=self.sidebar_area,
            fg_color=BrandColor.DARK_GRAY,
            corner_radius=0
        )
        self.sidebar_frame.pack(expand=True, fill=tk.BOTH, padx=0, pady=0)

        # メインフレームを生成
        self._frame_state.mainframes = {
            # トップページのメインフレーム
            UIString.TOP: TopPageFrame(
                parent=self.mainframe_area,
                root=self,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            ), 
            # チャットページのメインフレーム
            UIString.CHAT: ChatPageFrame(
                parent=self.mainframe_area,
                root=self,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            )
        }
        # メインフレームを全て設置する
        for frame in self._frame_state.mainframes.values():
            frame.grid(row=0, column=0, sticky='nsew')

    def get_current_mainframe_name(self):
        '''現在表示されているメインフレームの名前を返す'''
        return self._frame_state.current_mainframe

    def update_current_mainframe_name(self, new_current_mainframe: str):
        '''現在表示しているフレームの名前を設定する'''
        self._frame_state.current_mainframe = new_current_mainframe

    def update_sidebar_selected(self, selected):
        '''サイドバーのボタンを押さずに画面遷移した際、サイドバーの選択状況を更新する'''
        self.sidebar_frame.button_callback(selected)

    def show_frame(self, frame_name: str):
        '''引数で指定されたフレームを一番上に表示する'''
        frame = self._frame_state.mainframes[frame_name]
        frame.tkraise()

    def recreate_chatpage_frame(self):
        '''チャットページのフレームを作成し直して上書き、設置する'''
        self._frame_state.mainframes[UIString.CHAT] = ChatPageFrame(
                parent=self.mainframe_area,
                root=self,
                fg_color=BrandColor.GRAY,
                corner_radius=0
            )
        self._frame_state.mainframes[UIString.CHAT].grid(row=0, column=0, sticky='nsew')

    def get_messages_list(self):
        return self._messages_list

    def add_message(self, role, content):
        self._messages_list.append({'role': role, 'content': content})

    def get_generated_image(self):
        '''生成された画像をImageクラスで返す'''
        return Image.open(self._generated_image)

    def get_image_path(self):
        return self._generated_image

    def set_image_path(self, image):
        self._generated_image = image

    def get_generated_audio(self):
        return self._generated_audio

    def set_generated_audio(self, audio):
        self._generated_audio = audio

    def get_generated_video(self):
        return self._generated_video

    def get_webui_dir(self):
        return self._webui_dir

    def get_ai_chitchat_dir(self):
        return self._ai_chitchat_dir

    def remove_focus(self, event):
        '''クリックした場所が指定されたウィジェットではない場合、フォーカスを外す'''
        # フォーカスを外したいウィジェットの型
        widget_types = [tk.Text, tk.Entry, tk.Label, ct.CTkCanvas]
        if type(event.widget) not in widget_types:
            event.widget.master.focus_set()

    def set_tool_path(self):
        '''dir_path.txtからディレクトリのパスを読み込んで設定する'''
        webui_path = read_txt_file('dir_path.txt', 'webui')
        self._webui_dir = webui_path

    def fetch_generated_video(self):
        '''生成された最新動画のパスを取得する'''
        # 生成結果が格納されるディレクトリのパス
        result_dir = os.path.join(self._webui_dir, r'extensions\SadTalker\results')
        self._generated_video = fetch_latest_file(result_dir)


    ###デバッグ用###
    def make_audio(self):
        audio = AudioFileClip(self._generated_video)
        audio.write_audiofile('assets/sample/test.wav')
        audio.close()