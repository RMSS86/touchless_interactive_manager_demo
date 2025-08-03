import cv2
import mediapipe as mp
import pyautogui

from src.utils.old_version.modules.functional_modules._TIM_SWITCHER_ import _SWITCHER_
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
class AUTO_MOUSE():
    def __init__(self):
        self.hand_detector = mp.solutions.hands.Hands()
        self.screen_width, self.screen_height = pyautogui.size()
        self.index_y = 0
        self.AUTOMOUSE_COMMS = ['6', '7']
        self.tag_mouse_command_ = []

    def AUTO_mouse_(self, __ret, __source, __cv):

        while __ret:
            self.frame_height, self.frame_width, _ = __source.shape
            self.output = self.hand_detector.process(__source)

            if self.output.multi_hand_landmarks:
                for hand in self.output.multi_hand_landmarks:
                    self.landmarks = hand.landmark

                    for id, landmark in enumerate(self.landmarks):
                        x = int(landmark.x * self.frame_width)
                        y = int(landmark.y * self.frame_height)

                        if id == 8:
                            cv2.circle(img=__source, center=(x, y), radius=10, color=(0, 255, 255))
                            self.index_x = self.screen_width / self.frame_width * x
                            self.index_y = self.screen_height / self.frame_height * y
                            pyautogui.moveTo(self.index_x, self.index_y)

                        if id == 12:
                            cv2.circle(img=__source, center=(x, y), radius=10, color=(0, 255, 255))
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
                            cv2.circle(img=__source, center=(x, y), radius=10, color=(0, 255, 255))
                            self.thumb_x = self.screen_width / self.frame_width * x
                            self.thumb_y = self.screen_height / self.frame_height * y
                            #print('outside', abs(self.index_y - self.thumb_y))
                            if abs(self.index_y - self.thumb_y) < 50:
                                print('Okay Gesture')
                                # pyautogui.click()
                                # pyautogui.sleep(0.3)

            return __source
        return None


######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
#####
_SW_= _SWITCHER_()