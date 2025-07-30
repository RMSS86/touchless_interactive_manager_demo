from src.modules.hand_recognition.HAND_REC_DIGITS import HAND_REC_DIGITS
from src.phaser.PHASER import PHASER


class SWITCHER:
    def __init__(self, __cv):
        self.__cv = __cv
        self.signal_out = None

    def router(self, __sig_in):
        self.signal_out = _HR_.HandCounter(__sig_in, self.__cv)

        return self.signal_out


_HR_= HAND_REC_DIGITS() # //> BROADCASTING TO SELF SERVER ENGINE

