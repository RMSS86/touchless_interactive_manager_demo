from src.drawers.DRAWER import DRAWER
from src.phaser.PHASER import PHASER
import mediapipe as mp

#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####

class HAND_REC_DIGITS():
    def __init__(self):
        # self._results = None
        self.lmList = None
        self.handNo = None
        self.results = None
        self._img = None
        self.upcount = None
        self.count_ = None

        self.mpHands = mp.solutions.hands
        self.Hands = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mp.solutions.drawing_utils
        self.fingersCoordinate = [(8, 6), (12, 10), (16, 14), (20, 18)]
        self.thumbCoordinate = (4, 3)
        self._anti_counter = 0
        self.tag_hand_command_ = []

    def HandCounter(self, _vid, __cv):
        # //> INITIALIZING DRAWING FMO LOCAL RAW SIGNAL
        self.__cv = __cv
        _DW_ = DRAWER(self.__cv)

        # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
        while self.__cv.active():
            # //> DYNAMIC VARS
            self._img = _vid
            self.upcount = 0
            self.handNo = 0
            self.LH = 0
            self.RH = 1
            self.lmList = []
            self.incorrect_H = 'INCORRECT_HAND'

            # //> PASSING IMG TO MAIN PROCESSOR FOR TRACKING
            self.results = self.Hands.process(self._img)

            # //> ASSERT IF HAND IS RIGHT OR LEFT AND FILTERS ACTIONS
            if self.results.multi_hand_landmarks:  # //> GETS LANDMARK ON LH IF EXIST
                # //> ASSERTS IF HAND NNUMBER CONDITION IS MET AND RESOLVES
                if self.results.multi_handedness[0].classification[0].index == self.LH:

                    # //> [ 1 ]GETS RESULT FILTERED AND DRAWS TO UI WITH COLOUR CONDITION
                    self.Local_UI_drawer(self._img, self.results, _DW_)

                    # //> [ 2 ]MAKES PROXIMITY CALCULATION FOR COMMAND RESPONSE
                    for coordinate in self.fingersCoordinate:
                        if self.lmList[coordinate[0]][1] < self.lmList[coordinate[1]][1]:
                            self.upcount += 1

                    if self.lmList[self.thumbCoordinate[0]][0] > self.lmList[self.thumbCoordinate[1]][0]:
                        self.upcount += 1

                    # //> [ 3 ]COUNTS COMMAND RECEIVED AND PHASES IT
                    _PHASER_.Hand_CMD_Counter(self.upcount)

                # //> ASSERTS IF HAND NNUMBER CONDITION IS MET AND RESOLVES
                if self.results.multi_handedness[0].classification[0].index == self.RH:

                    # //> [ 1 ]GETS RESULT FILTERED AND DRAWS TO UI WITH COLOUR CONDITION
                    self.Local_UI_drawer(self._img, self.results, _DW_, _color='INC')

                    # //> [ 3 ]COUNTS COMMAND RECEIVED AND PHASES IT
                    _PHASER_.Hand_CMD_Counter(self.incorrect_H)

            return self._img
        return None

    def Local_UI_drawer(self, __img, __results, __dw, _color='COR'):
        # //> CLEANING UP LANDMARKS FROM RESULTS ARRAY
        for id, lm in enumerate(__results.multi_hand_landmarks[0].landmark):
            h, w, c = __img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)

            # //> ADD CLEAN LANDMARKS TO ARRAY
            self.lmList.append((cx, cy))

        # //> PASSES THE ARRAY TO EMBEDDED DRAWER W/ CONDITION
        __dw.DGT_point_drawer(__img, self.lmList,_color=_color)

_PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT







