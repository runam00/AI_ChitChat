from enum import Enum

class UIString(Enum):
    # メインフレーム
    TITLE = 'AI ChitChat'
    TAB_GENERATE = '作成'
    TAB_GALLERY = 'ギャラリー'
    PLACEHOLDER_GEN = 'AIに作成してほしいキャラクターの特徴を入力する'
    GENERATE = 'AI画像を生成する'
    SELECT_FROM_GALLERY = '選択した画像を使用する'
    SELECT_FROM_GENERATE = 'このキャラクターと話す'

    # サイドバー
    TOP = 'TOP'
    CHAT = 'CHAT'


    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]