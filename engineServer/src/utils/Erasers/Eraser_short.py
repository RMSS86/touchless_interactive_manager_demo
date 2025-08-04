from exceptiongroup import catch

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
routes = [{'R1': 'DIGITS', 'R2': 'CMDS', 'R3': 'FACEREC', 'R4': 'AUTOMOUSE', 'R5': 'SLEEP','R6': 'OFFLINE'}]
#
route = routes[0]['R1']
# //>  MATCH CASE
def route_selector(__RX):
    route = routes[0][__RX]

    return route

while True:
    __RX = input("Press enter a route from to quit {'R1': 'DIGITS', 'R2': 'CMDS', 'R3': 'FACEREC', 'R4': 'AUTOMOUSE', 'R5': 'SLEEP','R6': 'OFFLINE'}\n")

    try:
        route = routes[0][__RX]
    except:
        print("value incorrect select from {'R1': 'DIGITS', 'R2': 'CMDS', 'R3': 'FACEREC', 'R4': 'AUTOMOUSE', 'R5': 'SLEEP','R6': 'OFFLINE'}\n")


    match route:
        case 'DIGITS':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
            print(routes[0]['R1'])
        case 'CMDS':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
            print(routes[0]['R2'])
        case 'FACEREC':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
            print(routes[0]['R3'])
        case 'AUTOMOUSE':  # //> STARTS SINGLE LH DIGITS RECOGNITION COMMAND
            print(routes[0]['R4'])
        case _:
            print("[ Invalid ENTRY ]")

































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