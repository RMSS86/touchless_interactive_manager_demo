from src.camera.CAMERA_ import Camera
from src.database.DB_MANAGER import DB_MANAGER

# //> ML MODULES
import mediapipe as mp
import numpy as np
import face_recognition

# //> SYSTEM MODULE
import os

# //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
from sklearn.metrics.pairwise import cosine_similarity

# //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
RAW_IMG_SOURCE_PATH = '../../utils/data/faces/raw_images'

class FACE_RECOGNITION:
    def __init__(self, __cv, __mode='SS'):

        if __mode == 'SS':
            # //> [ 1.5 ]CREATION OF FACE DATA RAW_IMG_SOURCE_PATH,
            self.CLASS_NAMES, self._ENCODE_ = self.face_embeddings(RAW_IMG_SOURCE_PATH, __cv, True)
        # //> VAR_FOR_QUERIES
        self.encodedCurrentFrame = None
        self.faceCurrentFrame = None
        self.user_ID = '2'
        self._index_ = 0
        self.CATEGORIES = ['Load Entries']
        self.INITIAL_LISTS = ['Load Entries']
        self.array_dims = 128

        # //> INDEX ON FACE RECOGNITION INSTRUCTION MAP
        self._tag_counter_= []

        # //> COLOR SAMPLES
        self.tag_NameColor = (255, 255, 255)  # //> RGB for White
        self.square_Not_Color = (112, 112, 246)  # //> RGB for Red
        self.square_Fetching_Color = (230, 226, 109)  # //> RGB for Yellow
        self.square_Match_Color = (0, 255, 0)  # //> RGB for Green

        # //> TAGGING PARAMS
        self._nameTagFailed = '_UNKNOWN_'
        self._nameTagFetching = '_FETCHING_'

        # //> UI TABULATION PARAMS
        self._square_tag_factor = 4
        self._square_text_factor = 6
        self._eval_parser_factor = 3
        self._eval_parser_factor_fail= 3

        # //> MEDIAPIPE PARAMS
        self.static_image_mode = False
        self.max_num_faces = 1
        self.conf_ratio = 0.5
        self.results = None

        # //> BUFFER COUNT VARIABLES
        self.tag_face_command_= []
        self.slot_capacity = 8

        # //> MEDIAPIPE INITIALIZATION
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
                                        static_image_mode=self.static_image_mode,
                                        max_num_faces=self.max_num_faces,
                                        min_detection_confidence=self.conf_ratio)


    def FacialRotor(self, __cv, __mode='mAp'):

        # //> MAIN LOOP INITIALIZER
        while __cv.active(): # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR

            self.key_frame = __cv.keyframe() # //> SETTING GLOBAL KEY FRAMERS
            self._success, self._img = __cv.stream_() # //< RAW  FEED FROM CAMERA CLASS self.debug_image

            if __mode == 'mp':
                _CAM_.driver_().imshow('MP_MODE',self.MP_PROCESSOR(self._img, True))

            else:
                _CAM_.driver_().imshow('MP_MODE',self.FC_PROCESOR(self._img,True))


    def MP_PROCESSOR(self, __vid, __log=False):
        self.results = self.face_mesh.process(__vid)

        if self.results.multi_face_landmarks:

            if __log:
                print('Face Landmarks: {}'.format(self.results.multi_face_landmarks))

        return __vid


    def FC_PROCESOR(self, __vid, __log=False):
        # //> GETTING COORS FROM IMAGE REAL TIME
        self.faceCurrentFrame = face_recognition.face_locations(__vid)
        self.encodedCurrentFrame = face_recognition.face_encodings(__vid, self.faceCurrentFrame)

        if self.encodedCurrentFrame:

            if __log:
                print('faceCurrentFrame : {} {}'.format(self.faceCurrentFrame, self.encodedCurrentFrame[0].tolist()))

        return __vid


    def get_similarity(__target, __records, __names, __log=False):
        # //> PERFORM SIMILARITY COMPARISON USING
        # [ scikit-learn's cosine_similarity ]

        if __records:
            # //> GETS THE PROXIMITY OPERATION
            similarities = cosine_similarity([__target], __records)[0]

            # FINDS THE MOST SIMILAR FACE
            most_similar_index = np.argmax(similarities)

            if similarities[most_similar_index] > 0.7:  # test threshold

                if __log:
                    print(f"Identified as: {__names[most_similar_index]}")  # //> SHOULD BE EMP ID

                return __names[most_similar_index]
            else:
                print("Face not recognized.")
        else:
            print("No faces stored in the database.")


    # //> MAKES AND ARRAY FOR FACE LANDMARKS EMBEDDINGS
    def Face_embeddings_Counter(self, __count, __mode='SIMPLE'):
        self.tag_face_command_.append(__count)
        self.FACE_normalizer(self.tag_face_command_, self.slot_capacity)



    def FACE_normalizer(self, __embeddings, __slot_len=3):
        if len(__embeddings) == __slot_len:
            return __embeddings[-1]



    def face_embeddings(self, __face_loc='FAKE_DATA', __cv=None, __log=False):
        if __face_loc != 'FAKE_DATA':
            # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
            self.SOURCE_IMAGES = []
            self.CLASS_NAMES = []
            self.MYLIST = os.listdir(__face_loc)
            self.ENCODED_LIST = []

            for _cl in self.MYLIST:
                self._RawImg = __cv.imread(f'{__face_loc}/{_cl}')
                # //> ENCODED IMAGES TO BE ENCODED BY BULK OR SINGLE SHOTS(THIS CASE)
                self.SOURCE_IMAGES.append(self._RawImg)
                # //> CLEARS THE IMAGE NAME TO THE NAME NEED TO BE CHANGED IN EMP_ID
                self.CLASS_NAMES.append(os.path.splitext(_cl)[0])

            for _img in self.SOURCE_IMAGES:
                _img = __cv.cvtColor(_img, __cv.COLOR_BGR2RGB)

                self._ENCODE = face_recognition.face_encodings(_img)[0]
                self.ENCODED_LIST.append(self._ENCODE)

            if __log:
                print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES, self.ENCODED_LIST[0].tolist()))

            return self.CLASS_NAMES, self.ENCODED_LIST[0].tolist()

        if __face_loc == 'FAKE_DATA': # //> FOR DUMMY TESTING PURPOSES GENERATED DATA
            # //> GENERAL FICTION NAME
            self.CLASS_NAMES = ['John Doe']

            # //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
            self.ENCODED_LIST = np.random.rand(128).tolist()

            if __log:
                print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES, self.ENCODED_LIST))

            return self.CLASS_NAMES, self.ENCODED_LIST
        return None


_DBM_ = DB_MANAGER()
_CAM_ = Camera(0)  # //> PROMPTED CAMERA OBJECT WITH DEFAULT DEVICE
_FR_ = FACE_RECOGNITION(_CAM_.driver_())

_FR_.FacialRotor(_CAM_)

# FACE GETS EMBEDDED MAKES API CALL TO BACK END PROXIMITY VECTOR, RETURNS RESULT AND THEN COMPARES IN THE BACK GROUND IF THE SAME PERSON IS INFRONT THE SCREEN AND PROCEDES SOFT LOG OUT IF NOT.