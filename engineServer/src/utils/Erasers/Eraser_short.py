
# //> ML MODULES
import numpy as np
import face_recognition
# import mediapipe as mp

# //> SYSTEM MODULE
from datetime import datetime
from collections import Counter
import os

# //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
from sklearn.metrics.pairwise import cosine_similarity

from src.broadcaster.COM_IO import COMM_IO
from src.camera.CAMERA_ import Camera
from src.database.DB_MANAGER import DB_MANAGER
from src.modules.face_recognition.FACE_EMBEDDINGS import FACE_EMBEDDINGS


# //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
class FACE_RECOGNITION:
    def __init__(self, __cv, __mode='HYBRID',
                        __path='../data/faces/raw_images',
                         __db_settings='../../database/database.env'):

        #//> [ 0 ]DYNAMIC CALLABLE PATH FOR RAW IMAGES
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

            # //> [ 1.5 ]CREATION OF FACE DATA RAW_IMG_SOURCE_PATH
            self.CLASS_NAMES, self._ENCODE_ = _FR_EMB_.face_embeddings(self.RAW_IMG_SOURCE_PATH, __cv, True)

        if __mode == 'HYBRID':

            # //> [ 2 ]
            self._FACES_COLLECTION = _DBM_.FACES_COLLECTION
            self._STORED_EMBEDDINGS = _DBM_.STORED_EMBEDDINGS
            self._STORED_NAMES = _DBM_.STORED_NAMES
            print(' _STORED_EMBEDDINGS [ {} ] _STORED_NAMES {}'.format(len(self._STORED_EMBEDDINGS), self._STORED_NAMES))

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
        self._eval_parser_factor_fail = 3
        self._eval_parser_factor_not = 9

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

        # //> MEDIAPIPE PARAMS
        self.static_image_mode = False
        self.max_num_faces = 1
        self.conf_ratio = 0.5
        self.results = None

        # //> BUFFER COUNT VARIABLES
        self.tag_face_command_= []
        self._user_recd_counter_ = []
        self._user_not_rec_counter_ = []
        self._user_not_in_frame_counter_ = []
        self.slot_capacity = 3

        # //> COMMAND_REFERENCES
        self.USER_IDENTIFIED = "USER_IDENTIFIED"
        self.USER_NOT_RECOGNIZED_IN_DATABASE = "USER_NOT_RECOGNIZED_IN_DATABASE"
        self.NO_USER_FACE_RECOGNIZED_IN_FRAME = "NO_USER_FACE_RECOGNIZED_IN_FRAME"
        self.NO_FACES_STORED_IN_DATABASE = "NO_FACES_STORED_IN_DATABASE"
        self.UNABLE_TO_GET_NEW_USER_STORED_IN_DATABASE = "UNABLE_TO_GET_NEW_USER_STORED_IN_DATABASE"

    # //> MAIN ENGINE #TODO: MODIFY TO FIT SWITCHER
    def FacialRotor(self): # __vid, __ret

        # //< TODO: DUPLICATE INCOMING SIGNAL AND SPLIT PROCESSING AND LET RETURN CLEAN BACK TO SWITCHER
        while _CAM_.active(): # __ret  # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
            self.key_frame = _CAM_.keyframe()  # //> SETTING GLOBAL KEY FRAMERS
            self._success, self.debug_image, = _CAM_.stream_()  # //< RAW  FEED FROM CAMERA CLASS self.debug_image

            # //> SELECTS MODE TO OPERATIVE PROCESSING
            self.debug_image = self._FD_SELF_HYBRID_MODE(self.debug_image, False)

            # //< TODO: REMOVE TO FIT SWITCHER
            _CAM_.driver_().imshow('MP_MODE', self.debug_image)

            # //> RETURN PROCESSED IMAGE BACK TO THREAD
            # return self.debug_image # //< TODO: MODIFY TO FIT SWITCHER


    def _FD_SELF_HYBRID_MODE(self, _img, __log=True):

        try:
            # //> GETS TIME AND EMBEDDINGS FOR MULTIPLE PURPOSE THREADS
            self.now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            self.encodedCurrentFrame = face_recognition.face_encodings(_img)

            # //> MERE FACE RECOGNITION COUNT / COMMAND PURPOSES
            self.Face_embeddings_Counter(self.encodedCurrentFrame[0].tolist(), "SIMPLE")

            # //> UI PICTURE TO SELF
            # //< TODO: MAKE FACE CROPPER METHOD TO SEND CROPPED IMAGE TO UI / GET USER PICTURE DISP
            # //> TODO: [CONT] >>> self.faceCurrentFrame = face_recognition.face_locations(self._img)

            if __log:
                print("CURRENT FACIAL LANDMARKS: {} \nAT [ {} ]".format(
                    self.encodedCurrentFrame[0].tolist(), self.now))

        except Exception as e:
            print('{}'.format(self.NO_USER_FACE_RECOGNIZED_IN_FRAME))
            # //> WHEN USER NOT IN SIGNAL, INFORM UI AND TAKE ACTION USER_NOT_IN_FRAME
            self.USER_Phaser('NONE', self._eval_parser_factor_not, self.NO_USER_FACE_RECOGNIZED_IN_FRAME)

            self.TAG_RESETER_()

        return _img


    # //> MAKES AND ARRAY FOR FACE LANDMARKS EMBEDDINGS
    def get_similarity(self, __target, __records, __names, __log=True):
        # //> PERFORM SIMILARITY COMPARISON USING [ scikit-learn's cosine_similarity ]
        if __records:

            # //> GETS THE PROXIMITY OPERATION
            self.similarities = cosine_similarity([__target], __records)[0]

            if __log:
                print('similarities: [ {} ]'.format(self.similarities))

            # FINDS THE MOST SIMILAR FACE
            self.most_similar_index = np.argmax(self.similarities)

            if self.similarities[self.most_similar_index] > 0.9:  # testing threshold

                if __log:
                    print('most_similar_index: [ {} ]'.format(self.most_similar_index))
                    print(f"USER_IDENTIFIED_AS: {__names[self.most_similar_index]}")  # //> SHOULD BE EMP ID

                # # //> WHEN USER RECOGNIZED INFORM UI AND TAKE ACTION
                self.USER_Phaser(__names[self.most_similar_index], self._eval_parser_factor, self.USER_IDENTIFIED )

                return __names[self.most_similar_index]

            else:
                print(self.USER_NOT_RECOGNIZED_IN_DATABASE)

                # # //> WHEN USER NOT RECOGNIZED INFORM UI AND TAKE ACTION USER_IDENTIFIED
                self.USER_Phaser('NONE', self._eval_parser_factor_fail, self.USER_NOT_RECOGNIZED_IN_DATABASE)
                return self.USER_NOT_RECOGNIZED_IN_DATABASE

        else:
            print(self.NO_FACES_STORED_IN_DATABASE)
            return self.NO_FACES_STORED_IN_DATABASE


    # //> GETS PHASE OF FACES RECOGNIZED TO ENABLE API FETCH
    def FACE_normalizer(self, __embeddings, __slot_len, __log=False):

        # //> PHASER LEN EVALUATION
        if len(__embeddings) == __slot_len:

            if __log:
                print('LAST CONTINUOUS FACE REC: {}'.format(__embeddings[-1]))

            # //> MAKE COMPARISON ON LOCAL CALLED DB RECORDS
            self.get_similarity(__embeddings[-1] , self._STORED_EMBEDDINGS, self._STORED_NAMES, False)

            # //> RESETS COUNTER TO DEFAULT
            self.TAG_RESETER_()


    # //> COUNTS INCOMING OBJS AND APPLIES LOGICAL ACTION
    def Face_embeddings_Counter(self, __count, __mode='SIMPLE'):
        if __count:
            # //> INCOMING USER EMBEDDINGS IN
            self.tag_face_command_.append(__count)
            self.FACE_normalizer(self.tag_face_command_, self.slot_capacity, False)

        else:
            # //> RESETS TAGGER
            self.TAG_RESETER_()


    # //> ADDING A NEW USER FROM DATA
    def ADD_new_user(self, __user, __log=False):
        try:
            # //> INGESTS NEW COMPOSED USER AND ADDS DATA TO DB
            _DBM_.insert_new_user(__user, True)

        except Exception as e:
            print("{} ERROR {}".format(self.UNABLE_TO_GET_NEW_USER_STORED_IN_DATABASE, e))

        try:
            # //> FRESH FETCH TO DATABASE [ UPDATED DATA CHECKPOINT ]
            self._db, self._collection = _DBM_.get_db_settings(self.DB_SETTINGS_LOCAL_PATH, True)
            _DBM_.fetch_whole_db_to_Local(self._db, self._collection ,True)

        except Exception as e:
            print("{} ERROR {}".format(self.UNABLE_TO_GET_NEW_USER_STORED_IN_DATABASE, e))


    # //> CONTINUOUS PHASE / COMM COMMANDER 'REC' / 'NOT'
    def USER_Phaser(self, _id, _parser, _comm):
        # //> TODO: WHEN THE USER IS LOG OUT TO VERIFY AND USER IS ABOUT TO TAKE ACTION [LOG-OUT/PUNCH AUX]
        # //> WHEN USER IS RECOGNIZED
        if _comm == self.USER_IDENTIFIED:
            self._user_recd_counter_.append(_id)
            if len(self._user_recd_counter_) == _parser:

                counter__ = Counter(self._user_recd_counter_)  # //> GET BUFFER ANALYSIS
                if len(counter__) == 1:

                    # //> GET THIS REQUESTS ORGANIZED ON COMM-IO
                    _value__, __count_of_ = counter__.most_common()[0]
                    _COMM_.universal_COMM_Receiver_(
                        _value__,'API_USER',
                        self.USER_IDENTIFIED,'UI_UPDATE')

                    # TODO: PROVE THAT LOGGED USER STILL LOGGED WHEN MAKING DECISIONS ON THE FLOW
                    # TODO: WHEN RECOGNIZING A FACE, GOT TO USER PAGE AUTOMATICALLY [CREATE A UI_DO COMMAND]
                    self.USER_RESETER_()

        # //> WHEN USER IS NOT BEING RECOGNIZED
        if _comm ==  self.USER_NOT_RECOGNIZED_IN_DATABASE:
            self._user_not_rec_counter_.append(_id)
            if len(self._user_not_rec_counter_) == _parser:

                # //> GET THIS REQUESTS ORGANIZED ON COMM-IO
                _COMM_.universal_COMM_Receiver_(
                    self.USER_NOT_RECOGNIZED_IN_DATABASE,
                    'API_USER', self.USER_NOT_RECOGNIZED_IN_DATABASE, 'UI_UPDATE')

                # TODO: MAKING A LOG OUT WHEN NO USER IN_FRONT PAGE FOR AS LONG AS 15SECS / MODE TO HOME PAGE
                # TODO: CREATE USER_LOGGING_LOG COLLECTION
                self.USER_RESETER_()


        # //> WHEN USER IS NOT IN FRAME
        if _comm == self.NO_USER_FACE_RECOGNIZED_IN_FRAME:
            self._user_not_in_frame_counter_.append(_id)
            if len(self._user_not_in_frame_counter_) == _parser:

                # //> GET THIS REQUESTS ORGANIZED ON COMM-IO
                _COMM_.universal_COMM_Receiver_(self.NO_USER_FACE_RECOGNIZED_IN_FRAME, 'API_USER', self.NO_USER_FACE_RECOGNIZED_IN_FRAME, 'UI_UPDATE')

                # TODO: MAKING A LOG OUT WHEN NO USER IN_FRONT PAGE FOR AS LONG AS 15SECS / MODE TO HOME PAGE
                self.USER_RESETER_()


    # //> RESETS SHORT COUNT ONLY
    def USER_RESETER_(self):
        self._user_recd_counter_ = []
        self._user_not_rec_counter_ = []
        self._user_not_in_frame_counter_ = []


    # //> RESETS LONG AND FACE COUNT ONLY
    def TAG_RESETER_(self):
        self._tag_counter_ = []
        self.tag_face_command_ = []

    # //> LOGGERS?

_CAM_ = Camera(0) # //> CAMERA INITIALIZATION
_DBM_ = DB_MANAGER() # //> DB_MANAGER INITIALIZATION
_FR_EMB_ = FACE_EMBEDDINGS() # //> FACE_EMBEDDINGS INITIALIZATION
_COMM_ = COMM_IO() # //> COMM_IO INITIALIZATION

_FR_ = FACE_RECOGNITION(_CAM_.driver_()) # //> FACE_RECOGNITION INITIALIZATION

if __name__ == '__main__':
    _FR_.FacialRotor()


# //> TODO: SWITCHER ON MODE MECHANISM! [URGENT]
# [local]TODO: #1

# with open('../../modules/hand_recognition/keypoint_classifier/keypoint_classifier_label.csv',
#           encoding='utf-8-sig') as f:
#     keypoint_classifier_labels = csv.reader(f)
#     keypoint_classifier_labels = [
#         row[0] for row in keypoint_classifier_labels
#     ]

# print('FROM ERASER!',keypoint_classifier_labels)
#
#
#
# routes = [{'R1': 'DIGITS', 'R2': 'CMDS', 'R3': 'FACEREC', 'R4': 'AUTOMOUSE', 'R5': 'SLEEP','R6': 'OFFLINE'}]
#
# CATEGORIES = [{'':'',}]
#
# CMD_TYPE = [ 'ACTIONS', 'CMD', 'RESET', 'TOGGLE' ]
#
# MODES = ['LOGIN','AUTO_MOUSE','CMD_OPTS', 'CMD_STEPPER']
#
# LOGIN = {}
#
# AUTO_MOUSE= {}
#
# CMD_OPTS = {}
#
# CMD_STEPPER = {}
#
#
# _CMD = {
#     'CMD_TYPE': 'CMD',
#     'MODE': 'CMD_OPTS',
#     'CMD_BODY':
#         {
#            '_CMD': '',
#         }
# }

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

# route = routes[0]['R1']
# # //>  MATCH CASE
# def route_selector(__RX):
#     route = routes[0][__RX]
#     return route
#
# while True:
#     __RX = input("Press enter a route from to quit {'R1': 'DIGITS', 'R2': 'CMDS', 'R3': 'FACEREC', 'R4': 'AUTOMOUSE', 'R5': 'SLEEP','R6': 'OFFLINE'}\n")
#
#     try:
#         route = routes[0][__RX]
#     except:
#         print("value incorrect select from {'R1': 'DIGITS', 'R2': 'CMDS', 'R3': 'FACEREC', 'R4': 'AUTOMOUSE', 'R5': 'SLEEP','R6': 'OFFLINE'}\n")
#
#
#     match route:
#         case 'DIGITS':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R1'])
#         case 'CMDS':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R2'])
#         case 'FACEREC':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R3'])
#         case 'AUTOMOUSE':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R4'])
#         case _:
#             print("[ Invalid ENTRY ]")

































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