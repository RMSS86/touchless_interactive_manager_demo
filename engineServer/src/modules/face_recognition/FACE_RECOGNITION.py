
# //> ML MODULES
import numpy as np
import face_recognition
# import mediapipe as mp

# //> SYSTEM MODULE
from datetime import datetime
import os

# //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
from sklearn.metrics.pairwise import cosine_similarity

from src.camera.CAMERA_ import Camera
from src.database.DB_MANAGER import DB_MANAGER

# //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES

class FACE_RECOGNITION:
    def __init__(self, __cv, __mode='HYBRID',
                 __path='../data/faces/raw_images', __db_settings='../../database/database.env'):

        #//> DYNAMIC CALLABLE PATH FOR RAW IMAGES
        self._collection = None
        self._db = None
        self._success = None
        self.most_similar_index = None
        self.similarities = None
        self.RAW_IMG_SOURCE_PATH = __path
        self.DB_SETTINGS_LOCAL_PATH = __db_settings

        self._img = None
        self.key_frame = None
        self.debug_image = None
        if __mode == 'SS':
            # //> [ 1.5 ]CREATION OF FACE DATA RAW_IMG_SOURCE_PATH,
            self.CLASS_NAMES, self._ENCODE_ = self.face_embeddings(self.RAW_IMG_SOURCE_PATH, __cv, True)

        if __mode == 'HYBRID':

            self._FACES_COLLECTION = _DBM_.FACES_COLLECTION
            self._STORED_EMBEDDINGS = _DBM_.STORED_EMBEDDINGS
            self._STORED_NAMES = _DBM_.STORED_NAMES
            print(' _STORED_EMBEDDINGS {} _STORED_NAMES {}'.format(self._STORED_EMBEDDINGS, self._STORED_NAMES))

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
        self._eval_parser_factor = 3
        self._eval_parser_factor_fail= 3

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
        self._user_recd_counter_ = []
        self.slot_capacity = 3

    def FacialRotor(self): # __vid, __ret

        while _CAM_.active(): # __ret  # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
            self.key_frame = _CAM_.keyframe()  # //> SETTING GLOBAL KEY FRAMERS
            self._success, self.debug_image, = _CAM_.stream_()  # //< RAW  FEED FROM CAMERA CLASS self.debug_image

            # //>
            self.debug_image = self._FD_SELF_HYBRID_MODE(self.debug_image, False)

            # //>
            _CAM_.driver_().imshow('MP_MODE', self.debug_image)
            # return self.debug_image


    def _FD_SELF_HYBRID_MODE(self, _img, __log=True):
        # self.faceCurrentFrame = face_recognition.face_locations(self._img)
        try:
            self.now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            self.encodedCurrentFrame = face_recognition.face_encodings(_img)
            self.Face_embeddings_Counter(self.encodedCurrentFrame[0].tolist(), "SIMPLE")

            if __log:
                print("CURRENT FACIAL LANDMARKS: {} \nAT [ {} ]".format(
                    self.encodedCurrentFrame[0].tolist(), self.now))

        except Exception as e:
            print('OOPS {}'.format(e))
            self.TAG_RESETER_()

        return _img

    # //> MAKES AND ARRAY FOR FACE LANDMARKS EMBEDDINGS
    def get_similarity(self, __target, __records, __names, __log=False):
        # //> PERFORM SIMILARITY COMPARISON USING [ scikit-learn's cosine_similarity ]
        if __records:

            # //> GETS THE PROXIMITY OPERATION
            self.similarities = cosine_similarity([__target], __records)[0]

            if __log:
                print('similarities: [ {} ]'.format(self.similarities))

            # FINDS THE MOST SIMILAR FACE
            self.most_similar_index = np.argmax(self.similarities)

            if self.similarities[self.most_similar_index] > 0.7:  # testing threshold

                if __log:
                    print('most_similar_index: [ {} ]'.format(self.most_similar_index))
                    print(f"USER_IDENTIFIED_AS: {__names[self.most_similar_index]}")  # //> SHOULD BE EMP ID

                return __names[self.most_similar_index]

            else:
                print("USER_NOT_RECOGNIZED_IN_DATABASE")
                return "USER_NOT_RECOGNIZED_IN_DATABASE"

        else:
            print("NO_FACES_STORED_IN_DATABASE")
            return "NO_FACES_STORED_IN_DATABASE"

    # //> GETS PHASE OF FACES RECOGNIZED TO ENABLE API FETCH
    def FACE_normalizer(self, __embeddings, __slot_len, __log=False):

        # //> PHASER LEN EVALUATION
        if len(__embeddings) == __slot_len:

            if __log:
                print('LAST CONTINUOUS FACE REC: {}'.format(__embeddings[-1]))

            # //> MAKE COMPARISON ON LOCAL CALLED DB RECORDS
            self.get_similarity(__embeddings[-1] , self._STORED_EMBEDDINGS, self._STORED_NAMES,True)
            # //> RESETS COUNTER TO DEFAULT
            self.TAG_RESETER_()

    # //>
    def Face_embeddings_Counter(self, __count, __mode='SIMPLE'):
        if __count:

            self.tag_face_command_.append(__count)
            self.FACE_normalizer(self.tag_face_command_, self.slot_capacity)

        else:

            self.TAG_RESETER_()

    # //> GETS LOCAL DATA FOTO FOR INGESTION> EMBEDDING DATA / NAME(USER_ID)
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
                print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES,
                                                                            self.ENCODED_LIST[0].tolist()))
            # //> RETURNS NORMALIZED VALUES
            return self.CLASS_NAMES, self.ENCODED_LIST[0].tolist()

        if __face_loc == 'FAKE_DATA':  # //> FOR DUMMY TESTING PURPOSES GENERATED DATA
            # //> GENERAL FICTION NAME
            self.CLASS_NAMES = ['John Doe']

            # //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
            self.ENCODED_LIST = np.random.rand(128).tolist()

            if __log:
                print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES, self.ENCODED_LIST))

            return self.CLASS_NAMES, self.ENCODED_LIST
        return None

    def ADD_new_user(self, __user, __log=False):
        try:
            # //> INGESTS NEW COMPOSED USER AND ADDS DATA TO DB
            _DBM_.insert_new_user(__user, True)

        except Exception as e:
            print("UNABLE_TO_GET_NEW_USER_STORED_IN_DATABASE, ERROR {}".format(e))

        try:
            # //> FRESH FETCH TO DATABASE [ UPDATED DATA CHECKPOINT ]
            self._db, self._collection = _DBM_.get_db_settings(self.DB_SETTINGS_LOCAL_PATH, True)
            _DBM_.fetch_whole_db_to_Local(self._db, self._collection ,True)

        except Exception as e:
            print("UNABLE_TO_GET_NEW_USER_STORED_IN_DATABASE, ERROR {}".format(e))

    # //> CONTINUOUS PHASE / COMM COMMANDER
    def USER_Phaser(self,_id, _parser, _comm):
        self._user_recd_counter_.append(_id)
        print(self._user_recd_counter_)
        if len(self._user_recd_counter_) == _parser:
            # TODO: ADD COMMIO ENTRY HERE!
            # TODO: PROVE THAT LOGGED USER STILL LOGGED WHEN MAKING DESICIONS ON THE FLOW
            # TODO: MAKING A LOG OUT WHEN NO USER INFRONT PAGE FOR AS LONG AS 15SECS / MODE TO HOME PAGE
            # TODO: WHEN RECOGNIZING A FACE, GOT TO USER PAGE AUTOMATICALLY [CREATE A UI_DO COMMAND]
            self.USER_RESETER_()

    def USER_RESETER_(self):
        self._user_recd_counter_ = []

    def TAG_RESETER_(self):
        self._tag_counter_ = []
        self.tag_face_command_ = []

_CAM_ = Camera(0)
_DBM_ = DB_MANAGER()
_FR_ = FACE_RECOGNITION(_CAM_.driver_())

if __name__ == '__main__':
    _FR_.FacialRotor()


# //> TODO: SWITCHER ON MODE MECHANISM! [URGENT]
# [local]TODO: #1
# FACE GETS EMBEDDED MAKES API CALL TO BACK END PROXIMITY VECTOR, RETURNS RESULT AND THEN COMPARES IN THE BACK GROUND IF THE SAME PERSON IS INFRONT THE SCREEN AND PROCEDES SOFT LOG OUT IF NOT.

# //> COMMAND DICTIONARY GUIDE

# //> <<< LOGIC FLOW RULES >>> [HINTS BASIS] PLUS [ROUTER SCHEMA]
# //> ** [ 0 ] FACE_RECOGNITION ] FROM START UP DEFAULT
# //> ** [ 1 ] LEFT HAND ] DIGITS COMMANDS FOR MENU SELECTION[ONE OF MAX 6 OPTS]**
# //> ** [ 2 ] LEFT HAND ] OPEN / CLOSE > UP / DOWN FROM MULTI-SELECTION
# //> ** [ 3 ] LEFT HAND ] CLOSE 5 SECS(4 ROUNDS ON PHASE) GETS LOG_OUT ACTION BACK TO FACE_RECOGNITION MODE
# //> ** [ 4 ] LEFT HAND ] OPEN 5 SECS(4 ROUNDS ON PHASE) GETS MODE_CHANGE ACTION
# //> ** [ 5 ] LEFT HAND ] POINTER 5 SECS(4 ROUNDS ON PHASE) GETS BACK_SELECTION ACTION
# //> ** [ 6 ] RIGHT HAND ] OK / CLOSE > Y / N RESPECTIVELY
# //> ** [ 7 ] RIGHT HAND ] POINTER 5 LONG(3 ROUNDS ON PHASE) GETS AUTO_MOUSE MODE
# //> ** [ 8 ] RIGHT HAND ] AUTO_MOSE MODE OK 5 LONG(3 ROUNDS ON PHASE) GETS [GENERAL_MENU] MODE(LEFT HAND DIGITS OR CMDS?)
# //> ** [ 9 ]  ]

















# import mediapipe as mp
# import cv2
# from pymongo import MongoClient
# # Assuming you have a face embedding model/function, e.g., from 'face_recognition' library
# # from face_recognition import face_encodings, load_image_file
#
# # MongoDB Connection
# client = MongoClient("mongodb://localhost:27017/") # Replace with your MongoDB connection string
# db = client["face_recognition_db"]
# face_collection = db["face_embeddings"]
#
# # MediaPipe Face Mesh setup
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)
#
# def get_face_embedding(image_path):
#     # Load image and process with MediaPipe
#     image = cv2.imread(image_path)
#     results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#
#     if results.multi_face_landmarks:
#         # Extract landmarks and generate embedding (requires a separate face embedding model)
#         # For demonstration, let's assume a dummy embedding
#         dummy_embedding = [0.1, 0.2, 0.3, ...] # Replace with actual embedding generation
#         return dummy_embedding
#     return None
#
# def store_face_data(person_id, embedding, name):
#     face_collection.insert_one({"person_id": person_id, "embedding": embedding, "name": name})
#
# def recognize_face(new_face_embedding):
#     min_distance = float('inf')
#     recognized_person = None
#
#     for stored_face in face_collection.find():
#         stored_embedding = stored_face["embedding"]
#         # Calculate distance (e.g., Euclidean distance) between embeddings
#         distance = sum([(a - b)**2 for a, b in zip(new_face_embedding, stored_embedding)])**0.5
#         if distance < min_distance:
#             min_distance = distance
#             recognized_person = stored_face["name"]
#
#     # Set a threshold for recognition
#     if min_distance < 0.6: # Adjust threshold based on your embedding model and data
#         return recognized_person
#     return "Unknown"
#
# # Example Usage:
# # embedding = get_face_embedding("path/to/image.jpg")
# # if embedding:
# #     store_face_data("user123", embedding, "John Doe")
# #
# # # Later, for recognition:
# # new_embedding = get_face_embedding("path/to/new_image.jpg")
# # if new_embedding:
# #     recognized_name = recognize_face(new_embedding)
# #     print(f"Recognized: {recognized_name}")


# import cv2
#
# from src.camera.CAMERA_ import Camera
# from src.database.DB_MANAGER import DB_MANAGER
#
# # //> ML MODULES
# import numpy as np
# import face_recognition
# # import mediapipe as mp
#
# # //> SYSTEM MODULE
# import os
#
# # //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
# from sklearn.metrics.pairwise import cosine_similarity
#
# # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
# RAW_IMG_SOURCE_PATH = '../../utils/data/faces/raw_images'
#
# class FACE_RECOGNITION:
#     def __init__(self, __cv, __mode='SS'):
#
#         self._img = None
#         self.key_frame = None
#         self.debug_image = None
#         if __mode == 'SS':
#             # //> [ 1.5 ]CREATION OF FACE DATA RAW_IMG_SOURCE_PATH,
#             self.CLASS_NAMES, self._ENCODE_ = self.face_embeddings(RAW_IMG_SOURCE_PATH, __cv, True)
#
#         # //> VAR_FOR_QUERIES
#         self.encodedCurrentFrame = None
#         self.faceCurrentFrame = None
#         self.user_ID = '2'
#         self._index_ = 0
#         self.CATEGORIES = ['Load Entries']
#         self.INITIAL_LISTS = ['Load Entries']
#         self.array_dims = 128
#
#         # //> INDEX ON FACE RECOGNITION INSTRUCTION MAP
#         self._tag_counter_= []
#
#         # //> COLOR SAMPLES
#         self.tag_NameColor = (255, 255, 255)  # //> RGB for White
#         self.square_Not_Color = (112, 112, 246)  # //> RGB for Red
#         self.square_Fetching_Color = (230, 226, 109)  # //> RGB for Yellow
#         self.square_Match_Color = (0, 255, 0)  # //> RGB for Green
#
#         # //> TAGGING PARAMS
#         self._nameTagFailed = '_UNKNOWN_'
#         self._nameTagFetching = '_FETCHING_'
#
#         # //> UI TABULATION PARAMS
#         self._square_tag_factor = 4
#         self._square_text_factor = 6
#         self._eval_parser_factor = 3
#         self._eval_parser_factor_fail= 3
#
#         # //> MEDIAPIPE PARAMS
#         self.static_image_mode = False
#         self.max_num_faces = 1
#         self.conf_ratio = 0.5
#         self.results = None
#
#         # //> BUFFER COUNT VARIABLES
#         self.tag_face_command_= []
#         self.slot_capacity = 8
#         #
#         # # //> MEDIAPIPE INITIALIZATION
#         # self.mp_face_mesh = mp.solutions.face_mesh
#         # self.face_mesh = self.mp_face_mesh.FaceMesh(
#         #                                 static_image_mode=self.static_image_mode,
#         #                                 max_num_faces=self.max_num_faces,
#         #                                 smooth_landmarks = True,
#         #                                 min_detection_confidence=self.conf_ratio)
#         #
#
#
#     def FacialRotor(self, __cv, __mode='mAp'):
#
#         # //> MAIN LOOP INITIALIZER
#         while __cv.active(): # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
#             self.key_frame = __cv.keyframe() # //> SETTING GLOBAL KEY FRAMERS
#             self._success, self._img, self.debug_image, = __cv.stream_() # //< RAW  FEED FROM CAMERA CLASS self.debug_image
#
#             self.debug_image = self.FC_PROCESOR(self._img, self.debug_image, True)
#
#             _CAM_.driver_().imshow('MP_MODE', self.debug_image)
#
#
#
#     def FC_PROCESOR(self, __vid, __source, __log=False):
#         # //> GETTING COORS FROM IMAGE REAL TIME
#         # self.faceCurrentFrame = face_recognition.face_locations(__vid)
#         # self.encodedCurrentFrame = face_recognition.face_encodings(__vid, self.faceCurrentFrame)
#         self.faceCurrentFrame = face_recognition.face_locations(__vid)
#         self.encodedCurrentFrame = face_recognition.face_encodings(__vid)
#         if self.encodedCurrentFrame:
#
#             # self._frame_Tagger_(_image=__vid, _faceloc=self.faceCurrentFrame, _squarefac=self._square_tag_factor,
#             #                     _recfac=self._square_text_factor, _nametag=self._nameTagFetching,
#             #                     _reccol=self.square_Match_Color, _text_col=self.tag_NameColor, __cv=__cv.driver_())  # On Matched :)
#
#             if __log:
#                 # print('faceCurrentFrame : {} {}'.format(self.faceCurrentFrame, self.encodedCurrentFrame[0].tolist()))
#                 print('faceCurrentFrame : {} {}'.format(self.faceCurrentFrame, self.encodedCurrentFrame[0].tolist()))
#
#         return __source
#
#     # def _frame_Tagger_(self, _image, _faceloc, _squarefac, _recfac, _nametag, _reccol,_text_col,__cv, _squarezise=36,_boldsquare=1,_textsize=1,_textoutline=1):
#     #     y1, x2, y2, x1 = _faceloc
#     #     y1, x2, y2, x1 = y1 * _squarefac, x2 * _squarefac, y2 * _squarefac, x1 * _squarefac
#     #     __cv.rectangle(_image, (x1, y1), (x2, y2), _reccol, _boldsquare)
#     #     __cv.rectangle(_image, (x1, y2 - _squarezise), (x2, y2), _reccol, __cv.FILLED)
#     #     __cv.putText(_image, _nametag, (x1 + _recfac, y2 - _recfac), __cv.FONT_HERSHEY_COMPLEX_SMALL, _textsize, _text_col , _textoutline)
#
#     def get_similarity(self, __target, __records, __names, __log=False):
#         # //> PERFORM SIMILARITY COMPARISON USING
#         # [ scikit-learn's cosine_similarity ]
#
#         if __records:
#             # //> GETS THE PROXIMITY OPERATION
#             similarities = cosine_similarity([__target], __records)[0]
#
#             # FINDS THE MOST SIMILAR FACE
#             most_similar_index = np.argmax(similarities)
#
#             if similarities[most_similar_index] > 0.7:  # test threshold
#
#                 if __log:
#                     print(f"Identified as: {__names[most_similar_index]}")  # //> SHOULD BE EMP ID
#
#                 return __names[most_similar_index]
#             else:
#                 print("Face not recognized.")
#         else:
#             print("No faces stored in the database.")
#
#
#     # //> MAKES AND ARRAY FOR FACE LANDMARKS EMBEDDINGS
#     def Face_embeddings_Counter(self, __count, __mode='SIMPLE'):
#         self.tag_face_command_.append(__count)
#         self.FACE_normalizer(self.tag_face_command_, self.slot_capacity)
#
#
#
#     def FACE_normalizer(self, __embeddings, __slot_len=3):
#         if len(__embeddings) == __slot_len:
#             return __embeddings[-1]
#
#
#
#     def face_embeddings(self, __face_loc='FAKE_DATA', __cv=None, __log=False):
#         if __face_loc != 'FAKE_DATA':
#             # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
#             self.SOURCE_IMAGES = []
#             self.CLASS_NAMES = []
#             self.MYLIST = os.listdir(__face_loc)
#             self.ENCODED_LIST = []
#
#             for _cl in self.MYLIST:
#                 self._RawImg = __cv.imread(f'{__face_loc}/{_cl}')
#                 # //> ENCODED IMAGES TO BE ENCODED BY BULK OR SINGLE SHOTS(THIS CASE)
#                 self.SOURCE_IMAGES.append(self._RawImg)
#                 # //> CLEARS THE IMAGE NAME TO THE NAME NEED TO BE CHANGED IN EMP_ID
#                 self.CLASS_NAMES.append(os.path.splitext(_cl)[0])
#
#             for _img in self.SOURCE_IMAGES:
#                 _img = __cv.cvtColor(_img, __cv.COLOR_BGR2RGB)
#
#                 self._ENCODE = face_recognition.face_encodings(_img)[0]
#                 self.ENCODED_LIST.append(self._ENCODE)
#
#             if __log:
#                 print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES, self.ENCODED_LIST[0].tolist()))
#
#             return self.CLASS_NAMES, self.ENCODED_LIST[0].tolist()
#
#         if __face_loc == 'FAKE_DATA': # //> FOR DUMMY TESTING PURPOSES GENERATED DATA
#             # //> GENERAL FICTION NAME
#             self.CLASS_NAMES = ['John Doe']
#
#             # //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
#             self.ENCODED_LIST = np.random.rand(128).tolist()
#
#             if __log:
#                 print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES, self.ENCODED_LIST))
#
#             return self.CLASS_NAMES, self.ENCODED_LIST
#         return None
#
#
# _DBM_ = DB_MANAGER()
# _CAM_ = Camera(1)  # //> PROMPTED CAMERA OBJECT WITH DEFAULT DEVICE
# _FR_ = FACE_RECOGNITION(_CAM_.driver_())
#
# _FR_.FacialRotor(_CAM_)

