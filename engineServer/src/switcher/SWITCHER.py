from src.modules.auto_mouse.AUTO_MOUSE import AUTO_MOUSE
from src.modules.hand_recognition.HANDS_REC_CMD import HR_CMD_Engine_
from src.modules.hand_recognition.HAND_REC_DIGITS import HAND_REC_DIGITS
from src.navigator.NAVIGATOR import NAVIGATOR


class SWITCHER:
    def __init__(self, __cv):

        # //> FETCHING FRESH CV SIGNAL
        self.__cv = __cv
        self.signal_out = None

        # //> ROUTE INIT STATE[ DEFAULT ON FACE_RECOGNITION ]
        _NAV_.route_selector('R1')

    def router(self, __sig_in, __ret):

        # //> SELECTION FROM NAVIGATOR CLASS
        match _NAV_.route: # //> LOGICAL DECISION TREE FOR APP LIFE CYCLE STATE // MATCH CASE

            case 'DIGITS': # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
                self.signal_out = _HR_.HandCounter(__sig_in, self.__cv)

            case 'CMDS': # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
                self.signal_out = HR_CMD_.HandCounter(__ret, __sig_in, self.__cv)

            case 'FACE_REC': # //> COORDINATES THE ACTIVE API FACE RECOGNITION MODULE
                # //> [local]TODO: #1
                pass

            case 'AUTO-MOUSE': # //> CONTROLS GUI DIRECTLY THROUGH CV EMULATING A PHYSICAL MOUSE
                self.signal_out = _ATM_.AUTO_mouse_(__ret, __sig_in, self.__cv)

            case 'SLEEP': # //> GETS [ SE ] INTO SLEEP MODE(ON RASPBERRYPI)
                # //> [local]TODO: #2
                pass

            case 'OFFLINE': # //> SENDS COMMAND TO FRONT END TO CHANGE UI TO OFFLINE /  STOPS CV
                # //> [local]TODO: #3
                pass

            case _: # //> UN-IMPLEMENTED CASE
                print('NOT IMPLEMENTED ENTRY')

        return self.signal_out


_HR_= HAND_REC_DIGITS() # //> BROADCASTING TO SELF SERVER ENGINE
_ATM_ = AUTO_MOUSE() # //> CONTROLLING GUI ON A CV EMULATED MOUSE
HR_CMD_ = HR_CMD_Engine_() # //> DECODES HANDS 4WAY LR-RH COMMANDS
_NAV_ = NAVIGATOR()
# TODO: SEND TO [ FE ] COMMANDS REAL TIME
