# Face Recognition / Video Processing

import mediapipe as mp
from collections import Counter



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
        self.Hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.fingersCoordinate = [(8, 6), (12, 10), (16, 14), (20, 18)]
        self.thumbCoordinate = (4, 3)
        self._anti_counter = 0
        self.tag_hand_command_ = []

    def HandCounter(self, _vid, __cv):
        while __cv.active():  # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
            self._img = _vid

            self.upcount = 0
            self.handNo = 0
            self.lmList = []

            self.results = self.Hands.process(self._img)  # Processing Image for Tracking

            if self.results.multi_hand_landmarks:  # Getting Landmark(location) of Hands if Exists
                for id, lm in enumerate(self.results.multi_hand_landmarks[self.handNo].landmark):
                    h, w, c = self._img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.lmList.append((cx, cy))

                # TODO: MAKE IT A GENERIC CLASS
                for point in self.lmList:
                    __cv.driver_().circle(self._img, point, 1, (230, 226, 109) , __cv.driver_().FILLED)

                for coordinate in self.fingersCoordinate:
                    if self.lmList[coordinate[0]][1] < self.lmList[coordinate[1]][1]:
                        self.upcount += 1

                if self.lmList[self.thumbCoordinate[0]][0] > self.lmList[self.thumbCoordinate[1]][0]:
                    self.upcount += 1

                self.Hand_CMD_Counter(self.upcount)

            return self._img
        return None

    # TODO: MAKE IT A GENERIC CLASS
    def Hand_CMD_Counter(self,_count):
        self.tag_hand_command_.append(_count)
        if len(self.tag_hand_command_) == 12:
            self.count_ = Counter(self.tag_hand_command_)
            self.value_, self.count_of = self.count_.most_common()[0]
            # TODO: SEND COMMAND FROM HERE USING COMMAND BUILDER TO [ FE ]
            # _SW_._universal_COMM_Receiver_(self.tag_hand_command_[0])
            print(self.value_)
            self.counter_reset()

    def counter_reset(self):
        self.tag_hand_command_ = []




