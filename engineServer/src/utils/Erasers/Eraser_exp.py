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

# //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
from sklearn.metrics.pairwise import cosine_similarity

# //> [ 0 ]LOADS AN ENV FILE FROM REALTIVE PATH, >>> USE[--env-file ]IN DOCKER
dotenv_path = Path('../../../../env/serverengine.env')
load_dotenv(dotenv_path=dotenv_path)

# //> ACCESS ENVIRONMENT VARIABLES
ES_DATABASE_RAW_CONN_STRING = os.getenv("ES_DATABASE")
ES_MONGODB_USERNAME = os.getenv("ES_MONGODB_USERNAME")
ES_MONGODB_PASSWORD = os.getenv("ES_MONGODB_PASSWORD")

# //> [ 1 ]TARGET STRINGS IN ES_DATABASE_RAW_CONN_STRING TO REPLACE
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

# //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
SAMPLE_EMBEDDING = np.random.rand(128).tolist()

# //> [ 2 ]POINTER FOR SERVER DB AND COLLECTION
DB_ = MONGO_CLIENT['test'] # //> REPLACE WITH FINAL DB
FACES_COLLECTION = DB_['users'] # //> REPLACE WITH FINAL COLLECTION

# //> [ 3 ]DUMMY USER DATA FOR TESTING PURPOSES
FACE_DUMMY_DATA = {
    "user_id": "user123",
    "name": "John Doe",
    "account": "Tigers_IX",
    "position": "Supervisor",
    "embedding": SAMPLE_EMBEDDING
}

# //> INSERTS A RECORD FOR NEW OBJECT
# FACES_COLLECTION.insert_one(FACE_DUMMY_DATA)

# //> FETCHES ALL OBJECTS UNDER THE FACES_COLLECTION DB
STORED_FACES_ALL = list(FACES_COLLECTION.find({}))

# //> MAKES PARALLEL ARRAYS FOR STORED_EMBEDDINGS, STORED_NAMES
STORED_EMBEDDINGS = [doc['embedding'] for doc in STORED_FACES_ALL]
STORED_NAMES = [doc['name'] for doc in STORED_FACES_ALL]

print('STORED_EMBEDDINGS {} \nSTORED_NAMES {}'.format(STORED_EMBEDDINGS, STORED_NAMES))

# //> PERFORM SIMILARITY COMPARISON USING [ scikit-learn's cosine_similarity ]

# if STORED_EMBEDDINGS:
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