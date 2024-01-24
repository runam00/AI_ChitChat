import customtkinter as ct

class FrameState:
    def __init__(self):
        self.__current_mainframe: str = ''  # 現在表示されているメインフレーム
        self.__mainframes: dict[str: ct.CTkFrame] = {}  # 画面遷移で使用するためのメインフレーム

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