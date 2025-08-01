from src.modules.hand_recognition.HANDS_REC_CMD import HR_CMD_Engine_
from src.modules.hand_recognition.HAND_REC_DIGITS import HAND_REC_DIGITS


class SWITCHER:
    def __init__(self, __cv):
        self.__cv = __cv
        self.signal_out = None

        self.routes =[{'R1': 'DIGITS', 'R2': 'CMDS',
                       'R3': 'FACE_REC', 'R4': 'AUTO-MOUSE',
                       'R5': 'SLEEP','R6': 'OFFLINE'}]

        self.route = self.routes[0]['R2']

    def router(self, __sig_in, __ret):
        # //> LOGICAL DECISION TREE FOR APP LIFE CYCLE STATE

        # //>  MATCH CASE
        match self.route:
            case 'DIGITS': # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
                self.signal_out = _HR_.HandCounter(__sig_in, self.__cv)

            case 'CMDS': # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
                self.signal_out = HR_CMD_.HandCounter(__ret, __sig_in, self.__cv) # __ret, __source, __debugImg, __cv
            case _:
                print("Invalid ENTRY")

        return self.signal_out

    # //> FUNCTION CHANGES VALUE OF ROUTE TO SWITCH DYNAMICALLY THE MODE
    def route_selector(self, __RX):
        self.route = self.routes[0][__RX]
        return self.route

_HR_= HAND_REC_DIGITS() # //> BROADCASTING TO SELF SERVER ENGINE

HR_CMD_ = HR_CMD_Engine_()