from collections import Counter
from collections import deque
from src.modules.hand_recognition.utils.Ryote import RYOTE
from src.phaser.PHASER import PHASER

class GST_MANAGER_:
    def __init__(self):
        # //> INIDIAL INDEX
        self.active = True
        self.L_index = 0
        self.R_index = 1
        self.send_L = False
        self.send_R = False

        # //> SIDE REFERENCING VALUES
        self.history_length = 16
        self.mostCMMN_L = None
        self.mostCMMN_R = None
        self.current_CMD_ = None

        # //> SIGN RESULT INIT
        self.hand_sign_id = None

        # //> [ ! ]ALT MECHANISM FOR PHASER METHOD
        self.point_history = deque(maxlen=self.history_length)
        self.command_history_L = deque(maxlen=self.history_length)
        self.command_history_R = deque(maxlen=self.history_length)

    def _handedness_(self, __source, __results, __hander, __dw, __log=False):

        # //> _CHANNEL_ LISTENING TO THE LEFT HAND [ HIDARI-TE ]
        if __hander.classification[0].index == self.L_index:
            # //> [ 1 ]UI HELPER FOR PRINTING THE DOTS OF USERS' HANDS
            __dw.CMD_BH_points_drawer(__source, __results, __hander.classification[0].index)
            # //> [ 2 ]PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
            self.hand_sign_id = _RYOTE_.processor_(__source, __results)
            # //> [ 3 ]COUNTS COMMAND RECEIVED AND PHASES IT
            _PHASER_.BH_CMD_Counter(self.hand_sign_id,__hander)

        # //> _CHANNEL_ LISTENING TO THE RIGHT HAND [ MIGI-TE ]
        if __hander.classification[0].index == self.R_index:
            # //> [ 1 ]UI HELPER FOR PRINTING THE DOTS OF USERS' HANDS
            __dw.CMD_BH_points_drawer(__source, __results, __hander.classification[0].index)
            # //> [ 2 ]PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
            self.hand_sign_id = _RYOTE_.processor_(__source, __results)
            # //> [ 3 ]COUNTS COMMAND RECEIVED AND PHASES IT
            _PHASER_.BH_CMD_Counter(self.hand_sign_id,__hander)

        # //> EVALUATION MODE TODO: [ PENDING ]

    # //> [ ! ]FOR EVALUATION MODE ONLY
    def Reset_Count(self):
        self.send_R = False
        self.send_L = False

_PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT
_RYOTE_ = RYOTE() # //> HANDS RECOGNITION MODULE

