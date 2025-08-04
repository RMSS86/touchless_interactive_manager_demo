from collections import deque
import mediapipe as mp
import numpy as np
from src.camera.CAMERA_ import Args
from src.drawers.DRAWER import DRAWER
from src.modules.hand_recognition.utils.GST_Manager import GST_MANAGER_
from src.modules.hand_recognition.utils.Ryote import RYOTE
from src.phaser.PHASER import PHASER


class HR_CMD_Engine_():
    def __init__(self, __handsCount=2):
        self.lmList = None
        self.hand_sign_id = None
        self.pre_processed_landmark_list = None
        self.landmark_list = None
        self._brect = None
        self._results = None
        self.key = None
        self.active = True
        self.handsNumber = __handsCount
        self.history_length = 16
        self.debug_image = None
        self._img = None

        self.no_hands_in_frame_CMD = 'NO_HANDS_IN_FRAME'
        self.no_hands_in_frame_message = '[ NO HANDS DETECTED ]'

        self.LH = 0
        self.RH = 1

        # //> BRECT DRAWING CONST
        self._padding = 21

        # //> SCOPE ARGUMENTS UNPACKING
        self._args = Args.get_args_mp()
        self._use_static_image_mode = self._args.use_static_image_mode
        self._min_detection_confidence = self._args.min_detection_confidence
        self._min_tracking_confidence = self._args.min_tracking_confidence
        self._use_brect = True

        # //> HANDS MODULE INITIALIZATION
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            static_image_mode=self._use_static_image_mode,
            max_num_hands=self.handsNumber,
            min_detection_confidence=self._min_detection_confidence,
            min_tracking_confidence=self._min_tracking_confidence,)

        self.finger_gesture_history = deque(maxlen=self.history_length)

    def HandCounter(self, __ret, __source, __cv, __log=False):
        # //> FETCHING FRESH SIGNAL
        self.__cv = __cv
        _DW_ = DRAWER(self.__cv)

        if __ret: # //> IF SIGNAL WAS FETCHED
            # //> HANDS MODULE GREEN FLAG TO ACTION
            __source.flags.writeable = False
            self._results = self._hands.process(__source)
            __source.flags.writeable = True

            #  //> MULTI-HAND PROCESSING MODULE STAGE [ ACTIVE ]
            if self._results.multi_hand_landmarks is not None:

                # //> [1] UI HELPER FOR PRINTING THE DOTS TO USERS HANDS
                _DW_.CMD_BH_points_drawer(__source, self._results, self._results.multi_handedness[0].classification[0].index)

                # //> ENGINE RUNNING FOR MODULAR HAND RECOGNITION
                for self.hand_landmarks, self.handedness in zip(self._results.multi_hand_landmarks,
                                                                self._results.multi_handedness):

                    # //> [2] PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
                    self.hand_sign_id = _RYOTE_.processor_(__source, self.hand_landmarks)

                    if __log: # //> LOGGING TO CONSOLE
                        print('FROM THE CMD_MANAGER HAND {} COMMAND {}'.format(self.handedness.classification[0].index, self.hand_sign_id))

                    # //> [5] SIGN COMBINATION INTERPRETER
                    _GSTM_._handedness_(self.handedness, self.hand_sign_id,True)

            else:
                # [local]TODO: #1
                _PHASER_.Hand_CMD_Counter(self.no_hands_in_frame_CMD)
                if __log: # //> LOGGING TO CONSOLE
                    print(' [ NO HANDS DETECTED ] ')

            return __source # //< ACTIVE RETURN OF PROCESSED SIGNAL BACK TO MAIN STREAMER->BROADCASTER TO [ BE ]
        return None


_RYOTE_ = RYOTE() # //> HANDS RECOGNITION MODULE
_GSTM_ = GST_MANAGER_() # //> COMMAND BY HANDEDNESS MODULE
_PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT

# [local]TODO: #1 # point_history.append([0, 0]) TODO: GET POINT HISTORY MODULE ON (FOR TZIJONEL)

# from collections import deque
# import mediapipe as mp
# import numpy as np
# from src.camera.CAMERA_ import Args
# from src.drawers.DRAWER import DRAWER
# from src.modules.hand_recognition.utils.GST_Manager import GST_MANAGER_
# from src.modules.hand_recognition.utils.Ryote import RYOTE
# from src.phaser.PHASER import PHASER
#
#
# class HR_CMD_Engine_():
#     def __init__(self, __handsCount=2):
#         self.lmList = None
#         self.hand_sign_id = None
#         self.pre_processed_landmark_list = None
#         self.landmark_list = None
#         self._brect = None
#         self._results = None
#         self.key = None
#         self.active = True
#         self.handsNumber = __handsCount
#         self.history_length = 16
#         self.debug_image = None
#         self._img = None
#
#         self.no_hands_in_frame_CMD = 'NO_HANDS_IN_FRAME'
#         self.no_hands_in_frame_message = '[ NO HANDS DETECTED ]'
#
#         self.LH = 0
#         self.RH = 1
#
#         # //> BRECT DRAWING CONST
#         self._padding = 21
#
#         # //> SCOPE ARGUMENTS UNPACKING
#         self._args = Args.get_args_mp()
#         self._use_static_image_mode = self._args.use_static_image_mode
#         self._min_detection_confidence = self._args.min_detection_confidence
#         self._min_tracking_confidence = self._args.min_tracking_confidence
#         self._use_brect = True
#
#         # //> HANDS MODULE INITIALIZATION
#         self._mp_hands = mp.solutions.hands
#         self._hands = self._mp_hands.Hands(
#             static_image_mode=self._use_static_image_mode,
#             max_num_hands=self.handsNumber,
#             min_detection_confidence=self._min_detection_confidence,
#             min_tracking_confidence=self._min_tracking_confidence,)
#
#         self.finger_gesture_history = deque(maxlen=self.history_length)
#
#     def HandCounter(self, __ret, __source, __cv, __log=False):
#         # //> FETCHING FRESH SIGNAL
#         self.__cv = __cv
#         _DW_ = DRAWER(self.__cv)
#
#         if __ret: # //> IF SIGNAL WAS FETCHED
#             # //> HANDS MODULE GREEN FLAG TO ACTION
#             __source.flags.writeable = False
#             self._results = self._hands.process(__source)
#             __source.flags.writeable = True
#
#             #  //> MULTI-HAND PROCESSING MODULE STAGE [ ACTIVE ]
#             if self._results.multi_hand_landmarks is not None:
#
#                 # //> [1] UI HELPER FOR PRINTING THE DOTS TO USERS HANDS
#                 _DW_.CMD_BH_points_drawer(__source, self._results)
#
#                 # //> ENGINE RUNNING FOR MODULAR HAND RECOGNITION
#                 for self.hand_landmarks, self.handedness in zip(self._results.multi_hand_landmarks,
#                                                                 self._results.multi_handedness):
#
#                     # //> [2] PREDICTS THE RESULT OF A HAND CLASSIFICATION PROCESS
#                     self.hand_sign_id = _RYOTE_.processor_(__source, self.hand_landmarks)
#
#                     if __log: # //> LOGGING TO CONSOLE
#                         print('FROM THE CMD_MANAGER HAND {} COMMAND {}'.format(self.handedness.classification[0].index, self.hand_sign_id))
#
#                     # //> [5] SIGN COMBINATION INTERPRETER
#                     _GSTM_._handedness_(self.handedness, self.hand_sign_id,True)
#
#             else:
#                 # [local]TODO: #1
#                 _PHASER_.Hand_CMD_Counter(self.no_hands_in_frame_CMD)
#                 if __log: # //> LOGGING TO CONSOLE
#                     print(' [ NO HANDS DETECTED ] ')
#
#             return __source # //< ACTIVE RETURN OF PROCESSED SIGNAL BACK TO MAIN STREAMER->BROADCASTER TO [ BE ]
#         return None
#
#
# _RYOTE_ = RYOTE() # //> HANDS RECOGNITION MODULE
# _GSTM_ = GST_MANAGER_() # //> COMMAND BY HANDEDNESS MODULE
# _PHASER_ = PHASER() # //> COUNTS ENTRIES AND PHASES RESULT

# [local]TODO: #1 # point_history.append([0, 0]) TODO: GET POINT HISTORY MODULE ON (FOR TZIJONEL)
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
# route = routes[0]['R1']
# # //>  MATCH CASE
# def route_selector(__RX):
#     route = routes[0][__RX]
#     print(route)
#
#     return route
#
# while True:
#     match route:
#         case 'DIGITS':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R1'])
#             route_selector('R2')
#         case 'CMDS':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R2'])
#         case 'FACEREC':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R3'])
#         case 'AUTOMOUSE':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
#             print(routes[0]['R4'])
#         case _:
#             print("Invalid ENTRY")
#
































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