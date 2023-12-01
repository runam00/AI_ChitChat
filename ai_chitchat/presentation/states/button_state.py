class ButtonState():
    def __init__(self, selected: str):
        # 初期値はトップページ
        self._selected: str = selected

    def selected(self):
        return self._selected

    def update_selected(self, selected):
        self._selected = selected