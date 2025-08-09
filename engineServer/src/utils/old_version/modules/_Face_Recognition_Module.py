# Face Recognition / Video Processing
import cv2
import numpy as np
import face_recognition
# Tensor FLow Lite-MediaPipe
import pyautogui

# System Module
import os


###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER
###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER
# from src.utils.old_version.modules.functional_modules.TIM_API_Module import UD_API
# from src.utils.old_version.modules.functional_modules._TIM_SWITCHER_ import _SWITCHER_
###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER
###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER

#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####
#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####
#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####
#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####FACE RECOGNITION#####
class FaceRecognition:
    def __init__(self):
        # TODO: Data Sources, in future replaced with a DF from SQL using the _Connection module AKA API
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        self.CATEGORIES = ['Load Entries']
        self.INITIAL_LISTS = ['Load Entries']
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        self.user_ID = '2'
        self._index_ = 0

        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        self._tag_counter_= []

        self.tag_NameColor = (255, 255, 255)  # RGB for White
        self.square_Not_Color = (112, 112, 246)  # RGB for Red
        self.square_Fetching_Color = (230, 226, 109)  # RGB for Yellow
        self.square_Match_Color = (0, 255, 0)  # RGB for Green

        self._nameTagFailed = '_UNKNOWN_'
        self._nameTagFetching = '_FETCHING_'

        self._square_tag_factor = 4
        self._square_text_factor = 6

        self._eval_pharser_factor = 3
        self._eval_pharser_factor_fail= 3

        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###

        ###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE
        self.COMMS = ['MOUSE', 'COUNT']
        self.bridge = self.COMMS[0]
        ###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE

        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        self.path = 'utils/Sources/Images/AttendingPeople'
        self.SourceImages = []
        self.ClassNames = []
        self.myList = os.listdir(self.path)  # Sets the path on disc for the images to take please before mounting.
        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        #(TO BE FIXED WITH MONGO OR POSGREsql IMPLEMENTATION!)

#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
        #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
        #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
        #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
        #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
        # print(self.myList)
        for cl in self.myList:
            self.RawImg = cv2.imread(f'{self.path}/{cl}')
            self.SourceImages.append(
                self.RawImg)  # Images to be encoded later this could be a single try to be updated or a bulk of photos to be updated from a database.
            self.ClassNames.append(
                os.path.splitext(cl)[0])  # Clears the name of the image to the name(need to be changed with EMP_ID)

        self._encodeListKnown_ = self._Coordinates()

        ####CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###
        ####CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###CONN###


    def findEncondings(self, Images):
        self.encondeList = []

        for img in Images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # print(img)
            self.encode = face_recognition.face_encodings(img)[0]
            self.encondeList.append(self.encode)

        print(f'Printed from findEncondings {self.encondeList}')
        return self.encondeList

    def _Coordinates(self):
        ###############Buider intergration from camera on Module faceRecognition
        # This used to be in Face_rotors!
        self.encodeListKnown = self.findEncondings(self.SourceImages)
        print(f'Printed from _Coordinates {self.encodeListKnown}')
        return self.encodeListKnown

    #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
    #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
    #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
    #######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!
#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!#######TO BE REPLACED AFTER API FULL IMPLEMENTATOION!!!


    ###FacialEncoder ###FacialEncoder ###FacialEncoder ###FacialEncoder ###FacialEncoder ###FacialEncoder
    ###FacialEncoder ###FacialEncoder ###FacialEncoder ###FacialEncoder ###FacialEncoder ###FacialEncoder
    def FacialRotor(self, _vid):
        ####IGNITION FRAMER####IGNITION FRAMER####IGNITION FRAMER####IGNITION FRAMER####IGNITION FRAMER####
        ####IGNITION FRAMER####IGNITION FRAMER####IGNITION FRAMER####IGNITION FRAMER####IGNITION FRAMER####
        self._frame_ = _vid            ### self.cap = cv2.VideoCapture(0) ###OLD VERSION WITHOUT _SWITCHER_


        while True:

            #####GETTING IMAGE FROM VIDEO REAL TIME#####GETTING IMAGE FROM VIDEO REAL TIME
            #####GETTING IMAGE FROM VIDEO REAL TIME#####GETTING IMAGE FROM VIDEO REAL TIME
            self._frame_ = cv2.flip(self._frame_, 1)
            self.img = self._frame_
            self.IMG_frame = cv2.resize(self.img, (0, 0), None, 0.25, 0.25)   ####SIZES FRAMES TO ENTRANCE.
            self.IMG_frame = cv2.cvtColor(self.IMG_frame,cv2.COLOR_BGR2RGB)  ###Sets CV2 interface to RGB

            #####GETTING COORS FROM IMAGE REAL TIME#####GETTING COORS FROM IMAGE REAL TIME#####
            #####GETTING COORS FROM IMAGE REAL TIME#####GETTING COORS FROM IMAGE REAL TIME#####
            self.faceCurrentFrame = face_recognition.face_locations(self.IMG_frame)
            self.encodedCurrentFrame = face_recognition.face_encodings(self.IMG_frame, self.faceCurrentFrame)


            #TODO: USE THE SWITCHER TO CHANGE MODES DYNAMICALLY
            self._FD_SELF_STORAGE_MODE(face_CF=self.faceCurrentFrame, encoded_CF=self.encodedCurrentFrame ,encodedLK=self._encodeListKnown_)
            #self._FD_API_MODE(face_CF=self.faceCurrentFrame, encoded_CF=self.encodedCurrentFrame)

            # return self.img
            cv2.imshow('MP_MODE', self.img)

    def _FD_SELF_STORAGE_MODE(self, face_CF, encoded_CF, encodedLK):
        for self.encondedFace, self.FaceLoc in zip(encoded_CF, face_CF):
            self.matches = face_recognition.compare_faces(encodedLK, self.encondedFace)
            self.faceDis = face_recognition.face_distance(encodedLK, self.encondedFace)
            self.matchIndex = np.argmin(self.faceDis)

            if self.matches[self.matchIndex]:
                self._nameTag = self.ClassNames[self.matchIndex].upper()

                self._frame_Tagger_(_image=self.img, _faceloc=self.FaceLoc, _squarefac=self._square_tag_factor,
                                    _recfac=self._square_text_factor, _nametag= self._nameTag,
                                    _reccol=self.square_Match_Color, _text_col=self.tag_NameColor)  # On Matched :)

                self._eval_Phaser(_name=self._nameTag,_valparser=self._eval_pharser_factor, _comm=self.COMMS[1])

            else:
                self._frame_Tagger_(_image=self.img, _faceloc=self.FaceLoc, _squarefac=self._square_tag_factor,
                                    _recfac=self._square_text_factor, _nametag=self._nameTagFailed,
                                    _reccol=self.square_Not_Color, _text_col=self.tag_NameColor)#On Falied :(

                self._eval_Phaser(_name=self._nameTagFailed, _valparser=self._eval_pharser_factor_fail, _comm=self.COMMS[0])








#TODO: A1 USIGN THE PIL LIBRARY, CREATE A SNAPSHOT OF THE USERS FACE USIGN THE  y1, x2, y2, x1 = self.FaceLoc
#TODO: A1.2 (AND SHOW THE IMAGE TAKEN AT THE MOMENT OF THE API CALL WHEN THE API CALL COMES BACK)

#TODO: Create User Menu when recognized face on(use self storage mode to test on console),
    #TODO: Create INDEX of all moves, modes, menu and commands.
    #TODO: Create the menu cycle flow with commands on either symbols or postures with the posture module.
    #TODO: create rules, the options for moving thorugh modes

        #TODO: Login sesson auto close when owner of the account not infront scaner
        #TODO: NX to evaluate thorugh API and to show nametag Loading when Awaiting for API response on Inquiry


    #TODO:[ SPECIAL GRADE MISSOION: [ COMPLETE API MODE ]

    def _FD_API_MODE(self, face_CF, encoded_CF):
        self._api_matches = False
        self.api_nameTag = 'NONE'
        #TODO: while api calling turn the square yellow and green when certified
        self.api_calling = '<LOADING...>'#while x true for
    #TODO: add THE ANTI*SPOOFING METHOD TO ALL RECOGNITION
        ####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER###
        ####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER###
        _UD_._bridge_(current_frame=face_CF, encoded_frame=encoded_CF)
        ####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER###
        ####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER####NEXUS TO API-MONGO MANAGER###
        for self.FaceLoc in face_CF:

            #TODO: the return name tag plus the fetching state rectangle showing
            if self._api_matches:
                #TODO: THIS IS FOR FAILED SELF STORAGE MODE, PLEASE REFORMAT _nametag param FROM API CALL :)
                self._frame_Tagger_(_image=self.img, _faceloc=self.FaceLoc, _squarefac=self._square_tag_factor,
                                    _recfac=self._square_text_factor, _nametag=self._nameTagFailed,
                                    _reccol=self.square_Not_Color, _text_col=self.tag_NameColor)#OnGood Respone :)

            #TODO:MAKE THE API COUNTER SELF VERSION!!!!
            else:
                self._frame_Tagger_(_image=self.img, _faceloc=self.FaceLoc, _squarefac=self._square_tag_factor,
                                    _recfac=self._square_text_factor, _nametag=self._nameTagFailed,
                                    _reccol=self.square_Not_Color, _text_col=self.tag_NameColor)







    ####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER###
    ####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER####CV2 FRAMER###
    def _frame_Tagger_(self,_image,_faceloc, _squarefac, _recfac, _nametag, _reccol,_text_col,_squarezise=36,_boldsquare=1,_textsize=1,_textoutline=1):
        y1, x2, y2, x1 = _faceloc
        y1, x2, y2, x1 = y1 * _squarefac, x2 * _squarefac, y2 * _squarefac, x1 * _squarefac
        cv2.rectangle(_image, (x1, y1), (x2, y2), _reccol, _boldsquare)
        cv2.rectangle(_image, (x1, y2 - _squarezise), (x2, y2), _reccol, cv2.FILLED)
        cv2.putText(_image, _nametag, (x1 + _recfac, y2 - _recfac), cv2.FONT_HERSHEY_COMPLEX_SMALL, _textsize, _text_col , _textoutline)

    ####PARAM-EV FOR SELF STORAGE MODE####PARAM-EV FOR SELF STORAGE MODE####PARAM-EV FOR SELF STORAGE MODE######
    ####PARAM-EV FOR SELF STORAGE MODE####PARAM-EV FOR SELF STORAGE MODE####PARAM-EV FOR SELF STORAGE MODE######
    def _eval_Phaser(self,_name, _valparser, _comm):
        self._tag_counter_.append(_name)
        print(self._tag_counter_)
        if len(self._tag_counter_) == _valparser:
            self.bridge = _comm
            print('Mode get switched to:', self.bridge)
            self.TAG_RESETER_()

    def TAG_RESETER_(self):
        self._tag_counter_ = []


# _UD_ = UD_API()
# _SW_= _SWITCHER_()

