from src.drawers.DRAWER import DRAWER
from src.phaser.PHASER import PHASER
import mediapipe as mp

#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####

class HAND_REC_DIGITS():
    def __init__(self):
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

        # //> INITIALIZING DRAWING FMO RAW SIGNAL
        self.__cv = __cv
        _DW_ = DRAWER(self.__cv)

        # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
        while self.__cv.active():
            self._img = _vid
            self.upcount = 0
            self.handNo = 0
            self.lmList = []

            # //> PASSING IMG TO MAIN PROCESSOR FOR
            self.results = self.Hands.process(self._img)  # Processing Image for Tracking

            if self.results.multi_hand_landmarks:  # //> GETS LANDMARK ON LH IF EXIST
                for id, lm in enumerate(self.results.multi_hand_landmarks[self.handNo].landmark):
                    h, w, c = self._img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    self.lmList.append((cx, cy))

                _DW_.DGT_point_drawer(self._img, self.lmList)

                for coordinate in self.fingersCoordinate:
                    if self.lmList[coordinate[0]][1] < self.lmList[coordinate[1]][1]:
                        self.upcount += 1

                if self.lmList[self.thumbCoordinate[0]][0] > self.lmList[self.thumbCoordinate[1]][0]:
                    self.upcount += 1

                _PHASER_.Hand_CMD_Counter(self.upcount) # //> COUNTS COMMAND RECEIVED AND PHASES IT

            return self._img
        return None


_PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT
 # //>



