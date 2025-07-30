from src.modules.hand_recognition.HAND_REC_DIGITS import HAND_REC_DIGITS

class SWITCHER:
    def __init__(self):
        self.signal_out = None

    def router(self, __sig_in, __driver):
        self.signal_out = _HR_.HandCounter(__sig_in, __driver)

        return self.signal_out


_HR_= HAND_REC_DIGITS() # //> BROADCASTING TO SELF SERVER ENGINE
