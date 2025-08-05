from collections import deque
import mediapipe as mp
import numpy as np
from src.camera.CAMERA_ import Args
from src.drawers.DRAWER import DRAWER
from src.modules.hand_recognition.utils.GST_Manager import GST_MANAGER_
from src.modules.hand_recognition.utils.Ryote import RYOTE
from src.phaser.PHASER import PHASER


class HR_CMD_Engine_():
    def __init__(self, __handsCount=2):
        self.lmList = None
        self.hand_sign_id = None
        self.pre_processed_landmark_list = None
        self.landmark_list = None
        self._brect = None
        self._results = None
        self.key = None
        self.active = True
        self.handsNumber = __handsCount
        self.history_length = 16
        self.debug_image = None
        self._img = None

        # //> INDEXING
        self.LH = 0
        self.RH = 1

        # //> BRECT DRAWING CONST
        self._padding = 21

        # //> SIGN ID BY SIDE
        self.LH_hand_sign_id = None
        self.RH_hand_sign_id = None

        # //> COMMAND VALUES TO FOR BROADCASTING
        self.no_hands_in_frame_CMD = 'NO_HANDS_IN_FRAME'
        self.no_hands_in_frame_message = '[ NO HANDS DETECTED ]'

        # //> SCOPE ARGUMENTS UNPACKING
        self._args = Args.get_args_mp()
        self._use_static_image_mode = self._args.use_static_image_mode
        self._min_detection_confidence = self._args.min_detection_confidence
        self._min_tracking_confidence = self._args.min_tracking_confidence
        self._use_brect = True

        # //> HANDS MODULE INITIALIZATION
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            static_image_mode=self._use_static_image_mode,
            max_num_hands=self.handsNumber,
            min_detection_confidence=self._min_detection_confidence,
            min_tracking_confidence=self._min_tracking_confidence,)

        # //> TO BE IMPLEMENTED ON FUTURE VERSIONS [ HISTORY QUEUE ENGINE ]
        self.finger_gesture_history = deque(maxlen=self.history_length)

    def HandCounter(self, __ret, __source, __cv, __log=False):

        self.__cv = __cv # //> FETCHING FRESH SIGNAL
        _DW_ = DRAWER(self.__cv) # //> NEW DRAWER CLASS

        if __ret: # //> IF SIGNAL WAS FETCHED
            # //> HANDS MODULE GREEN FLAG TO ACTION
            __source.flags.writeable = False # //> OPENING
            self._results = self._hands.process(__source)
            __source.flags.writeable = True  # //> CLOSING

            #  //> MULTI-HAND PROCESSING MODULE STAGE [ ACTIVE ]
            if self._results.multi_hand_landmarks is not None:

                # //> [1] ENGINE RUNNING FOR MODULAR HAND RECOGNITION
                for self.hand_landmarks, self.handedness in zip(self._results.multi_hand_landmarks,
                                                                self._results.multi_handedness):

                    # //> [5] SIGN COMBINATION INTERPRETER
                    _GSTM_._handedness_(__source, self.hand_landmarks, self.handedness, _DW_, True)

            else:  # //> WHEN NO HANDS IN FRAME
                _PHASER_.BH_CMD_Counter(self.no_hands_in_frame_CMD, 'NO_HANDS_DETECTED') # [local]TODO: #1

            return __source # //< ACTIVE RETURN OF PROCESSED SIGNAL BACK TO MAIN STREAMER->BROADCASTER TO [ BE ]
        return None # //< ACTIVE RETURN OF PROCESSED SIGNAL BACK TO MAIN STREAMER-> BLOC UNREACHABLE

_GSTM_ = GST_MANAGER_() # //> COMMAND BY HANDEDNESS MODULE
_PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT

# [local]TODO: #1 #FUTURE NOTE TO MYSELF: barrel_history.append([0, 0])
#  TODO: GET POINT HISTORY MODULE ON (FOR TZIJONEL)