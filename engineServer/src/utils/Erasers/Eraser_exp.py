import numpy as np
# import mediapipe as mp
# import cv2 as _cv

# //> IMPORTS ENV READERS
from dotenv import load_dotenv
from pathlib import Path

# //> IMPORTS MONGO CLOUDS DB CLASSES
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

# //> LOADS AN ENV FILE FROM REALTIVE PATH, >>> USE[--env-file ]IN DOCKER
dotenv_path = Path('../../../../env/serverengine.env')
load_dotenv(dotenv_path=dotenv_path)

# //> ACCESS ENVIRONMENT VARIABLES
ES_DATABASE_RAW_CONN_STRING = os.getenv("ES_DATABASE")
ES_MONGODB_USERNAME = os.getenv("ES_MONGODB_USERNAME")
ES_MONGODB_PASSWORD = os.getenv("ES_MONGODB_PASSWORD")

# //> TARGET STRINGS IN ES_DATABASE_RAW_CONN_STRING TO REPLACE
ES_TEMPLATE_USER = '<db_user>'
ES_TEMPLATE_PWD = '<db_password>'

# //> REPLACES TEMPLATE TARGET STRINGS FROM ES_DATABASE_RAW_CONN_STRING FOR AUTH CONNECTION TO SERVER
ES_DATABASE_URL_CONN_STRING = ES_DATABASE_RAW_CONN_STRING.replace(ES_TEMPLATE_USER, ES_MONGODB_USERNAME).replace(ES_TEMPLATE_PWD, ES_MONGODB_PASSWORD)

# //> CREATES A NEW CLIENT AND CONNECTS TO SERVER
MONGO_CLIENT = MongoClient(ES_DATABASE_URL_CONN_STRING, server_api=ServerApi('1'))

try: # //> SEND PING ON A SUCCESSFUL CONNECTION
    MONGO_CLIENT.admin.command('ping')
    print("PING RESPONSE: CONNECTED TO MONGODB DATABASE")
except Exception as e:
    print(e)

# EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
SAMPLE_EMBEDDING = np.random.rand(128).tolist()

# db = MONGO_CLIENT['face_recognition_db']
# faces_collection = db['faces']

# //> POINTER FOR SERVER DB AND COLLECTION
DB_ = MONGO_CLIENT['test']
FACES_COLLECTION = DB_['users']

# //> DUMMY USER DATA FOR TESTING PORPUSES
FACE_DUMMY_DATA = {
    "user_id": "user123",
    "name": "John Doe",
    "embedding": SAMPLE_EMBEDDING
}
print('SAMPLE_EMBEDDING {}'.format(FACE_DUMMY_DATA))
#
# FACES_COLLECTION.insert_one(FACE_DUMMY_DATA)
#
# STORED_FACES_ALL = list(FACES_COLLECTION.find({}))



#
# faces_collection.insert_one(face_data)
# print("Face embedding stored successfully.")
#
# # ... (previous code for MongoDB connection) ...
#
# # Example target embedding for identification
# target_embedding = np.random.rand(128).tolist()
#
# # Retrieve all stored embeddings
# stored_faces = list(faces_collection.find({}))
# stored_embeddings = [doc['embedding'] for doc in stored_faces]
# stored_names = [doc['name'] for doc in stored_faces]
#
# # Perform similarity comparison (e.g., using scikit-learn's cosine_similarity)
# from sklearn.metrics.pairwise import cosine_similarity
#
# if stored_embeddings:
#     similarities = cosine_similarity([target_embedding], stored_embeddings)[0]
#
#     # Find the most similar face
#     most_similar_index = np.argmax(similarities)
#     if similarities[most_similar_index] > 0.7:  # Example threshold
#         print(f"Identified as: {stored_names[most_similar_index]}")
#     else:
#         print("Face not recognized.")
# else:
#     print("No faces stored in the database.")