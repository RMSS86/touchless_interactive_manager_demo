# Face Recognition / Video Processing
import cv2
import face_recognition
# Tensor FLow Lite-MediaPipe
import mediapipe as mp
import pyautogui
####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####
####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####
from src.utils.old_version.modules.functional_modules._TIM_SWITCHER_ import _SWITCHER_
####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####
####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####

#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
#####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####HAND RECOGNITION####
class HandRecongnition():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.Hands = self.mpHands.Hands()
        #self.mpDraw = mp.solutions.drawing_utils
        self.fingersCoordinate = [(8, 6), (12, 10), (16, 14), (20, 18)]
        self.thumbCoordinate = (4, 3)
        # self.cap = cv2.VideoCapture(0)  # Module reader.
        self._anti_counter = 0
        self.tag_hand_command_ = []

    def HandCounter(self, _vid):
        self._frame_Hand = _vid

        while True:
            self.upcount = 0
            self._frame_Hand = cv2.flip(self._frame_Hand, 1)
            self._img_ = self._frame_Hand
            # success, img = cap.read()  # reading Frame
            # img = imutils.resize(img, width=780)
            self.converted_image = cv2.cvtColor(self._img_, cv2.COLOR_BGR2RGB)  # converting BGR to RGB
            self.results = self.Hands.process(self.converted_image)  # Processing Image for Tracking
            self.handNo = 0
            self.lmList = []
            # TODO:wrap count validation functionality on the SWitcher!
            if self.results.multi_hand_landmarks:  # Getting Landmark(location) of Hands if Exists
                for id, lm in enumerate(self.results.multi_hand_landmarks[self.handNo].landmark):
                    h, w, c = self._img_.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.lmList.append((cx, cy))
                # for hand_in_frame in self.results.multi_hand_landmarks:  # looping through hands exists in the Frame
                #     self.mpDraw.draw_landmarks(self._img_, hand_in_frame,
                #                                self.mpHands.HAND_CONNECTIONS)  # drawing Hand Connections
                for point in self.lmList:
                    cv2.circle(self._img_, point, 3, (230, 226, 109) , cv2.FILLED)

                for coordinate in self.fingersCoordinate:
                    if self.lmList[coordinate[0]][1] < self.lmList[coordinate[1]][1]:
                        self.upcount += 1

                if self.lmList[self.thumbCoordinate[0]][0] > self.lmList[self.thumbCoordinate[1]][0]:
                    self.upcount += 1

                ####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####
                self.Hand_CMD_Counter(self.upcount)
                ####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####

            return self._img_

    def Hand_CMD_Counter(self,_count):
        self.tag_hand_command_.append(_count)
        if len(self.tag_hand_command_) == 4:
            _SW_._universal_COMM_Receiver_(self.tag_hand_command_[0])
            self.counter_reset()

    def counter_reset(self):
        self.tag_hand_command_ = []

####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####
_SW_= _SWITCHER_()
####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####COMMAND_SWITCH####
