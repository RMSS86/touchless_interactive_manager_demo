import os
import time

import numpy as np
import face_recognition
import cv2
import asyncio

class Test():
    def __init__(self):
        self.path = 'Sources/Images/AttendingPeople'
        self.SourceImages = []
        self.ClassNames = []
        self.myList = os.listdir(self.path)

        for cl in self.myList:
            self.RawImg = cv2.imread(f'{self.path}/{cl}')
            self.SourceImages.append(
                self.RawImg)  # Images to be encoded later this could be a single try to be updated or a bulk of photos to be updated from a database.
            self.ClassNames.append(
                os.path.splitext(cl)[0])  # Clears the name of the image to the name(need to be changed with EMP_ID)

        self._encodeListKnown_ = self._Coordinates()
        #print('RAW LIST OF ENCODIGS: ', self._encodeListKnown_)

        ####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!
        ####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!
        asyncio.run(self.API_Splitter(self._encodeListKnown_))           ####KEY STEP!
        ####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!
        ####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!####KEY STEP!



    def findEncondings(self, Images):
        self.encondeList = []

        for img in Images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # print(img)
            self.encode = face_recognition.face_encodings(img)[0]
            self.encondeList.append(self.encode)

        #print(f'Printed from findEncondings {self.encondeList}')
        return self.encondeList

    def _Coordinates(self):
        ###############Buider intergration from camera on Module faceRecognition
        # This used to be in Face_rotors!
        self.encodeListKnown = self.findEncondings(self.SourceImages)
        #print(f'Printed from _Coordinates {self.encodeListKnown}')
        return self.encodeListKnown

    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################

    async def API_Splitter(self, encoders):

        self.arg_lenght = int(len(encoders))
        self.raw_ueclidean_coors = []
        self.raw_ueclidean_coors_listed_pack = []

        for n in range(self.arg_lenght):
            self.encs = []

            for i in encoders[n]:
                self.encs.append(i)
            self.raw_ueclidean_coors.append(self.encs)

        await self._DIAL_TASK_driver(self.raw_ueclidean_coors)

    async def _DIAL_TASK_driver(self, list: list):
        self.single_enc = False
        self.inc_obj_len = int(len(list))

        print('ARRANGE LENGHT: ', self.inc_obj_len)
        print('LENGHT OF THE CLEANED OBJECT OF LISTS: ', list)

        #####ASSESMENT FOR SINGLE PERSON VS SENTINEL MODE#####
        if len(list) == 1:
            self.single_enc = True
        else:
            self.single_enc = False
        #####ASSESMENT FOR SINGLE PERSON VS SENTINEL MODE#####

        try:
            self.TASKS = [self.AUTO_MONGO_Dialer(list[COUNT]) for COUNT in range(self.inc_obj_len)]
            self.RESULT = await asyncio.gather(*self.TASKS, return_exceptions=True)
        except Exception as err:
            print(err)


    async def AUTO_MONGO_Dialer(self, ud_arg):
        print('TASK FROM AUTO_MONGO_Dialer STARTED')
        await asyncio.sleep(1.0)
        print('FROM MONGO AUTO DIALER: ', ud_arg)
        print('FROM AUTO_MONGO_Dialer TASK DONE')

        def UD_ARG(self, *args):
            pass
        # TODO: this returns value _UNKOWN_ if false or object jason object with agents info if true with values, this will connecto with the SWITCHER for puting in yellow the recognition box on a api call?


        # TODO: Create the Auto Dialer Function
        # TODO: cretae MONGO database, conn and agregator pipeline

        # TODO: Connect functionality on respose from DB to tags in facial rotor and validations
        # TODO: Create interactive menu workflow and integrate signs with Hand counter!
        # TODO: Find how to integrate to React Native
        # TODO: RECREATE EASY ASSETS MANANGER IN REACT NATIVE OR FLUTTER/DART ON SQL OR MONGO!!!

#TODO: remember to #1 get the loc for the name tags in order specific and #2 take tenooral snapshot of the face and save it, if on sentinel mode.


#_API_ = asyncio.run(asyncTEST_Main().TEST())
#_API_ =  Test()

if __name__ =='__main__':
    pass
    #_API_
    # asyncio.run(Test())
    # Test()



# for COUNT in range(self.inc_obj_len):
#     self.AUTO_MONGO_Dialer(list[COUNT])


# self.TASKS = [asyncio.create_task(self.AUTO_MONGO_Dialer(list[COUNT])) for COUNT in range(self.inc_obj_len)]
# self.DONE, self.PENDING = await asyncio.wait(self.TASKS)
#
# for TASK in self.DONE:
#     self.RESULT = TASK.result()

#
# class asyncTEST_Main():
#
#     def __init__(self):
#         self.START = time.perf_counter()
#         self.END = time.perf_counter()
#
#         self.TODO = ['MAKE QR', 'MAKE TRAX APP', 'MAKE LAN LEARNING APP']
#
#     async def DO_WORK(self, s: str, delauy_s: float =1.0):
#         print(s,'STARTED')
#         await asyncio.sleep(delauy_s)
#         print(s, 'DONE')
#
#     async def TEST(self):
#
#         self.TASKS = [ asyncio.create_task(self.DO_WORK(ITEM)) for ITEM in self.TODO]
#         self.DONE, self.PENDING = await asyncio.wait(self.TASKS)
#
#
#         print('PROCESS TOOK:', self.END- self.START, 'SECONDS')
#
#

##################################################
##################################################
##################################################
# # Face Recognition / Video Processing
# import cv2
# import numpy as np
# import face_recognition
# # Tensor FLow Lite-MediaPipe
# import mediapipe as mp
# import pyautogui
#
#
# ######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
# ######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
# ######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
# ######AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE####AUTO MOUSE######
# class AutoMouse():
#     def __init__(self):
#         self.hand_detector = mp.solutions.hands.Hands()
#         self.drawing_utils = mp.solutions.drawing_utils
#         self.screen_width, self.screen_height = pyautogui.size()
#         self.index_y = 0
#
#     # TODO:change to single finger mouse mode
#     def _auto_mouse_(self, _vid):
#         self.frame_ = _vid
#
#         while True:
#
#             self.frame_ = cv2.flip(self.frame_, 1)
#
#             self.frame_height, self.frame_width, _ = self.frame_.shape
#             self.rgb_frame = cv2.cvtColor(self.frame_, cv2.COLOR_BGR2RGB)
#             self.output = self.hand_detector.process(self.rgb_frame)
#             self.hands = self.output.multi_hand_landmarks
#             if self.hands:
#                 for hand in self.hands:
#                     self.drawing_utils.draw_landmarks(self.frame_, hand)
#                     self.landmarks = hand.landmark
#
#                     for id, landmark in enumerate(self.landmarks):
#                         x = int(landmark.x * self.frame_width)
#                         y = int(landmark.y * self.frame_height)
#                         if id == 8:
#                             cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
#                             self.index_x = self.screen_width / self.frame_width * x
#                             self.index_y = self.screen_height / self.frame_height * y
#
#                         if id == 4:
#                             cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
#                             self.thumb_x = self.screen_width / self.frame_width * x
#                             self.thumb_y = self.screen_height / self.frame_height * y
#                             print('outside', abs(self.index_y - self.thumb_y))
#                             if abs(self.index_y - self.thumb_y) < 30:
#                                 print('Click')
#                                 pyautogui.click()
#                                 pyautogui.sleep(0.3)
#                             elif abs(self.index_y - self.thumb_y) < 100:
#                                 pyautogui.moveTo(self.index_x, self.index_y)
#
#             # self.video_show = cv2.imshow('WebCam', self.img)  # Sets the image source 'webcam', the framed sourced functionnn img.
#             cv2.waitKey(1)  # set the frame rate to 1 for real time.(Never user 0 o more than 2!)
#             return self.frame_







# Face Recognition / Video Processing
import cv2
import numpy as np
import face_recognition
# Tensor FLow Lite-MediaPipe
import mediapipe as mp
import pyautogui

vid =cv2.VideoCapture(0)
# sucess, vid_ = vid.read()
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

    # TODO:change to single finger mouse mode
    def _auto_mouse_(self, _vid):
        #self.frame_ = _vid
        self.vid_ = _vid

        while True:
            sucess, self.frame_   = self.vid_.read()
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
                            print('outside', abs(self.index_y - self.thumb_y))
                            if abs(self.index_y - self.thumb_y) < 45:
                                print('Click')
                                pyautogui.click()
                                pyautogui.sleep(0.3)
                            # elif abs(self.index_y - self.thumb_y) > 300:
                            #     print('OK Gesture')

                        if id == 4:
                            cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
                            self.thumb_x = self.screen_width / self.frame_width * x
                            self.thumb_y = self.screen_height / self.frame_height * y
                            print('outside', abs(self.index_y - self.thumb_y))
                            if abs(self.index_y - self.thumb_y) < 45:
                                print('Okay Gesture')
                                pyautogui.click()
                                pyautogui.sleep(0.3)
            cv2.imshow('WebCam', self.frame_)  # Sets the image source 'webcam', the framed sourced functionnn img.
            cv2.waitKey(1)  # set the frame rate to 1 for real time.(Never user 0 o more than 2!)
            #return self.frame_





AutoMouse()._auto_mouse_(vid)
#
# if self.hands:
#     for hand in self.hands:
#         self.drawing_utils.draw_landmarks(self.frame_, hand)
#         self.landmarks = hand.landmark
#
#         for id, landmark in enumerate(self.landmarks):
#             x = int(landmark.x * self.frame_width)
#             y = int(landmark.y * self.frame_height)
#             if id == 8:
#                 cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
#                 self.index_x = self.screen_width / self.frame_width * x
#                 self.index_y = self.screen_height / self.frame_height * y
#
#             if id == 4:
#                 cv2.circle(img=self.frame_, center=(x, y), radius=10, color=(0, 255, 255))
#                 self.thumb_x = self.screen_width / self.frame_width * x
#                 self.thumb_y = self.screen_height / self.frame_height * y
#                 print('outside', abs(self.index_y - self.thumb_y))
#                 if abs(self.index_y - self.thumb_y) < 30:
#                     print('Click')
#                     pyautogui.click()
#                     pyautogui.sleep(0.3)
#                 elif abs(self.index_y - self.thumb_y) < 100:
#                     pyautogui.moveTo(self.index_x, self.index_y)