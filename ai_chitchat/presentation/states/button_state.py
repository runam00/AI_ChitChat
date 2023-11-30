class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class ButtonState(Singleton):
    def __init__(self, selected):
        self._selected = selected

    def selected(self):
        return self._selected