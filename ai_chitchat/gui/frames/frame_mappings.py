from ..theme.strings import UIString
from ..frames.top_mainframe import TopMainFrame

class FrameMapping:
    _MAPPING = {
        UIString.TOP: TopMainFrame,
    }

    @classmethod
    def get(cls, key):
        return cls._MAPPING.get(key)