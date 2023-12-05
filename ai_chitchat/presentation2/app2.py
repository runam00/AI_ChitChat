import customtkinter as ct

class App(ct.CTk):
    def __init__(self):
        super().__init__()
    
        self.title('AI_ChitChat')
        self.geometry('1200x600')

        # 2×1でグリッドを設定
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # サイドバー
        self.sidebar_frame = ct.CTkFrame(self, width=100)
        self.sidebar_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

        self.home_button = ct.CTkButton(self.sidebar_frame, text='TOP', command=lambda: self.change_frame('TOP'))
        self.home_button.grid(row=0, column=0)
        self.chat_button = ct.CTkButton(self.sidebar_frame, text='CHAT', command=lambda: self.change_frame('CHAT'))
        self.chat_button.grid(row=1, column=0)

        # メイン
        self.mainframe_area = ct.CTkFrame(master=self, corner_radius=0)
        self.mainframe_area.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')
        self.mainframe_area.columnconfigure(0, weight=1)
        self.mainframe_area.rowconfigure(0, weight=1)

        self.frames = {}

        # トップページ
        self.top_frame = ct.CTkFrame(self.mainframe_area, fg_color='#393E46', corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky='nsew')

        self.top_label = ct.CTkLabel(self.top_frame, text='TOP')
        self.top_label.pack()

        self.frames['TOP'] = self.top_frame

        # チャットページ
        self.chat_frame = ct.CTkFrame(self.mainframe_area, fg_color='#393E46', corner_radius=0)
        self.chat_frame.grid(row=0, column=0, sticky='nsew')

        self.chat_label = ct.CTkLabel(self.chat_frame, text='CHAT')
        self.chat_label.pack()

        self.frames['CHAT'] = self.chat_frame


    def change_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

if __name__=='__main__':
    app = App()
    app.mainloop()