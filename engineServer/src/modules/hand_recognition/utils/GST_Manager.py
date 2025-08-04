from collections import Counter
from collections import deque

from src.modules.hand_recognition.utils.Ryote import RYOTE
from src.phaser.PHASER import PHASER

class GST_MANAGER_:
    def __init__(self):
        self.active = True
        self.L_index = 0
        self.R_index = 1
        self.send_L = False
        self.send_R = False

        self.history_length = 16
        self.mostCMMN_L = None
        self.mostCMMN_R = None
        self.current_CMD_ = None

        self.hand_sign_id = None

        self.point_history = deque(maxlen=self.history_length)
        self.command_history_L = deque(maxlen=self.history_length)
        self.command_history_R = deque(maxlen=self.history_length)

    def _handedness_(self, __source, __results, __hander, __log=False):

        # //> _CHANNEL_ LISTENING TO THE LEFT HAND [ HIDARI-TE ]
        if __hander.classification[0].index == self.L_index:
            # //> [2] PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
            self.hand_sign_id = _RYOTE_.processor_(__source, __results)
            _PHASER_.BH_CMD_Counter(self.hand_sign_id,__hander)  # //> COUNTS COMMAND RECEIVED AND PHASES IT


        # //> _CHANNEL_ LISTENING TO THE RIGHT HAND [ MIGI-TE ]
        if __hander.classification[0].index == self.R_index:
            # //> [2] PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
            self.hand_sign_id = _RYOTE_.processor_(__source, __results)
            _PHASER_.BH_CMD_Counter(self.hand_sign_id,__hander)  # //> COUNTS COMMAND RECEIVED AND PHASES IT
            # //> TODO: IMPLEMENT BROADCASTER CMD


        # //> EVALUATION MODE


    def Reset_Count(self):
        self.send_R = False
        self.send_L = False

# TODO: IMPORT PHASRR AND BRADCASTER, CREATE A COMMAND COMPOUSER MODEL AND THE APPS LIFECYCLE(HARDWRITTEN)
_PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT
_RYOTE_ = RYOTE() # //> HANDS RECOGNITION MODULE

# if __log:  # //> LOGGING TO CONSOLE
#     print('FROM THE CMD_MANAGER HAND {} COMMAND {}'.format(self.handedness.classification[0].index, self.hand_sign_id))
