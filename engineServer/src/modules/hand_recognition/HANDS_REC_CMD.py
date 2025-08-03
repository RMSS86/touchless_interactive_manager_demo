from collections import deque
import mediapipe as mp
import numpy as np
from src.camera.CAMERA_ import Args
from src.drawers.DRAWER import DRAWER
from src.modules.hand_recognition.utils.GST_Manager import GST_MANAGER_
from src.modules.hand_recognition.utils.Ryote import RYOTE


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
        self.LH = 0
        self.RH = 1

        # //> BRECT DRAWING CONST
        self._padding = 21

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

        self.finger_gesture_history = deque(maxlen=self.history_length)

    def HandCounter(self, __ret, __source, __cv):

        self.__cv = __cv
        _DW_ = DRAWER(self.__cv)

        if __ret:

            # //> HANDS MODULE GREEN FLAG TO ACTION
            __source.flags.writeable = False
            self._results = self._hands.process(__source)
            __source.flags.writeable = True

            #  //> MULTI-HAND PROCESSING MODULE STAGE
            if self._results.multi_hand_landmarks is not None:

                # //> [1] UI HELPER FOR PRINTING THE DOTS TO USERS HANDS
                _DW_.CMD_BH_points_drawer(__source, self._results)

                # //> ENGINE RUNNING FOR MODULAR HAND RECOGNITION
                for self.hand_landmarks, self.handedness in zip(self._results.multi_hand_landmarks,
                                                                self._results.multi_handedness):

                    # //> [2] PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
                    self.hand_sign_id = _RYOTE_.processor_(__source, self.hand_landmarks)

                    print('FROM THE CMD_MANAGER HAND {} COMMAND {}'.format(self.handedness.classification[0].index, self.hand_sign_id))

                    # # //> [5] SIGN COMBINATION INTERPRETER
                    _GSTM_._handedness_(self.handedness, self.hand_sign_id,True)

            else:
                # point_history.append([0, 0]) TODO: GET POINT HISTORY MODULE ON
                print(' [ NO HANDS DETECTED ] ')

            #########################################################################
            # //< ACTIVE RETURN OF PROCESSED SIGNAL BACK TO MAIN STREAMER->BROADCASTER TO [ BE ]
            return __source
        return None


_RYOTE_ = RYOTE()
_GSTM_ = GST_MANAGER_()
