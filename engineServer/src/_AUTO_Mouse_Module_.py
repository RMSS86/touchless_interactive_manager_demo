# Face Recognition / Video Processing
import cv2
import numpy as np
import face_recognition
# Tensor FLow Lite-MediaPipe
import mediapipe as mp
import pyautogui

from _TIM_SWITCHER_ import _SWITCHER_
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
class AutoMouse():
    def __init__(self):
        self.hand_detector = mp.solutions.hands.Hands()
        #self.drawing_utils = mp.solutions.drawing_utils
        self.screen_width, self.screen_height = pyautogui.size()
        self.index_y = 0
        self.AUTOMOUSE_COMMS = ['6' , '7']
        self.tag_mouse_command_ = []

    def _auto_mouse_(self, _vid):
        self.frame_ = _vid

        while True:
            self.frame_ = cv2.flip(self.frame_, 1)
            self.frame_height, self.frame_width, _ = self.frame_.shape
            self.rgb_frame = cv2.cvtColor(self.frame_, cv2.COLOR_BGR2RGB)
            self.output = self.hand_detector.process(self.rgb_frame)
            self.hands = self.output.multi_hand_landmarks

            if self.hands:
                for hand in self.hands:
                    #self.drawing_utils.draw_landmarks(self.frame_, hand)
                    self.landmarks = hand.landmark

                    for id, landmark in enumerate(self.landmarks):
                        x = int(landmark.x * self.frame_width)
                        y = int(landmark.y * self.frame_height)

                        if id == 8:
                            cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
                            self.index_x = self.screen_width / self.frame_width * x
                            self.index_y = self.screen_height / self.frame_height * y
                            pyautogui.moveTo(self.index_x, self.index_y)

                        if id == 12:
                            cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
                            self.thumb_x = self.screen_width / self.frame_width * x
                            self.thumb_y = self.screen_height / self.frame_height * y
                            #print('outside', abs(self.index_y - self.thumb_y))
                            if abs(self.index_y - self.thumb_y) < 50:
                                print('Click')#NORMAL CLICK FUNCTION
                                pyautogui.click()
                                pyautogui.sleep(0.3)
                            elif abs(self.index_y - self.thumb_y) < 100:
                                pass#TODO:create command #7 from anular finger or any other fingar in conjunction(if needed)

                        if id == 4:
                            cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
                            self.thumb_x = self.screen_width / self.frame_width * x
                            self.thumb_y = self.screen_height / self.frame_height * y
                            #print('outside', abs(self.index_y - self.thumb_y))
                            if abs(self.index_y - self.thumb_y) < 50:
                                print('Okay Gesture')
                                self.Hand_CMD_Counter(self.AUTOMOUSE_COMMS[0])
                                # pyautogui.click()
                                # pyautogui.sleep(0.3)

            return self.frame_

    def Hand_CMD_Counter(self,_count):
        self.tag_mouse_command_.append(_count)
        if len(self.tag_mouse_command_) == 4:
            _SW_._universal_COMM_Receiver_(self.tag_mouse_command_[0])
            self.counter_reset()

    def counter_reset(self):
        self.tag_mouse_command_ = []
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
#####
_SW_= _SWITCHER_()