# import cv2
import mediapipe as mp
import pyautogui

from src.phaser.PHASER import PHASER


######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
class AUTO_MOUSE():
    def __init__(self):
        self.hand_detector = mp.solutions.hands.Hands()
        self.screen_width, self.screen_height = pyautogui.size()
        self.radius_ = 9
        self.index_y = 0
        self.AUTOMOUSE_COMMS = ['6', '7']
        self.AUTOMOUSE_CMDS = ['CLICK', 'OK_MENU']
        self.no_hands_in_frame_CMD = 'NO_HANDS_IN_FRAME'
        self.no_hands_in_frame_message = '[ NO HANDS DETECTED ]'
        self.no_hands_in_frame_CMD = ''
        self.tag_mouse_command_ = []

    def AUTO_mouse_(self, __ret, __source, __cv, __log=False):

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
                            __cv.driver_().circle(img=__source, center=(x, y), radius=self.radius_ , color=(0, 255, 255))
                            self.index_x = self.screen_width / self.frame_width * x
                            self.index_y = self.screen_height / self.frame_height * y
                            pyautogui.moveTo(self.index_x, self.index_y)

                        if id == 12:
                            __cv.driver_().circle(img=__source, center=(x, y), radius=self.radius_ , color=(0, 255, 255))
                            self.thumb_x = self.screen_width / self.frame_width * x
                            self.thumb_y = self.screen_height / self.frame_height * y

                            if __log:
                                print('outside', abs(self.index_y - self.thumb_y))

                            if abs(self.index_y - self.thumb_y) < 50:
                                # //> MAKES CLICK TO UI AND SENDS NOTIFICATION TO UI
                                _PHASER_.Auto_Mouse_Manager(self.AUTOMOUSE_CMDS[0],
                                                           self.output.multi_handedness[0].classification[0].label.upper())
                                pyautogui.click()
                                pyautogui.sleep(0.3)

                            # elif abs(self.index_y - self.thumb_y) < 100:
                            #     # //> [local]TODO: #1
                            #     pass


                        if id == 4:
                            __cv.driver_().circle(img=__source, center=(x, y), radius=self.radius_ , color=(0, 255, 255))
                            self.thumb_x = self.screen_width / self.frame_width * x
                            self.thumb_y = (self.screen_height /
                                            self.frame_height * y)

                            if __log:
                                print('outside', abs(self.index_y - self.thumb_y))

                            if abs(self.index_y - self.thumb_y) < 42:
                                # //> STATES THE OK TO MENU OPTION
                                _PHASER_.Auto_Mouse_Manager(self.AUTOMOUSE_CMDS[1],
                                                           self.output.multi_handedness[0].classification[0].label.upper())

            return __source

        return __source



######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
#####
_PHASER_ = PHASER(_log=True) # //> COUNTS ENTRIES AND PHASES RESULT


# TODO: #1 CREATE CMD #7 FROM ANGULAR FINGER OR ANY OTHER IN CONJUNCTION(if needed)
