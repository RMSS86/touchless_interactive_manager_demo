
# Face Recognition / Video Processing
import cv2
# import face_recognition
# Tensor FLow Lite-MediaPipe
import mediapipe as mp
import pyautogui

from src.utils.old_version.modules.functional_modules._TIM_SWITCHER_ import _SWITCHER_
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