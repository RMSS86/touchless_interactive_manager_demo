import numpy as np
import cv2
import face_recognition

# //> IMPORTS ENV READERS
from dotenv import load_dotenv
from pathlib import Path

# //> IMPORTS MONGO CLOUDS DB CLASSES
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

# //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
from sklearn.metrics.pairwise import cosine_similarity

# //> DEVELOPMENT VARS
DB_CONNECT = True
USER_CREATE_NEW = False

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



# //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
RAW_IMG_SOURCE_PATH = '../data/faces/raw_images'
SOURCE_IMAGES = []
CLASS_NAMES = []
MYLIST = os.listdir(RAW_IMG_SOURCE_PATH)

# //> GETS PICTURES IN RAW FOLDER, MUST BE JUST ONE AT TIME FOR NOW, THEN
# //> CREATE A MECHANISM THAT COMPARES NAMES AND SELECTS THOSE NOT REGISTERED...
for cl in MYLIST:
    _RAW_IMG = cv2.imread(f'{RAW_IMG_SOURCE_PATH}/{cl}')
    # //> ENCODED IMAGES TO BE ENCODED BY BULK OR SINGLE SHOTS(THIS CASE)
    SOURCE_IMAGES.append(_RAW_IMG)
    # //> CLEARS THE IMAGE NAME TO THE NAME NEED TO BE CHANGED IN EMP_ID
    CLASS_NAMES.append(os.path.splitext(cl)[0])

# //> CREATE NEW RECORD
if USER_CREATE_NEW:
    def findEncondings(__images):
        # TODO: MAKE MULTIPLE / SINGLE MODE?
        ENCODED_LIST = []
        _ENCONDE = None

        for img__ in __images:
            img__ = cv2.cvtColor(img__, cv2.COLOR_BGR2RGB)

            _ENCONDE = face_recognition.face_encodings(img__)[0]
            ENCODED_LIST.append(_ENCONDE)
        #
        # print(f'Printed from findEncondings {ENCODED_LIST}')
        return ENCODED_LIST # // [0].tolist()
        # return _ENCONDE # //> FOR SINGLE MODE ARRAY


    _ENCONDE_ = findEncondings(SOURCE_IMAGES)

# //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
# SAMPLE_EMBEDDING = np.random.rand(128).tolist()


# //> [ 2 ]POINTER FOR SERVER DB AND COLLECTION
DB_ = MONGO_CLIENT['test'] # //> REPLACE WITH FINAL DB
FACES_COLLECTION = DB_['users'] # //> REPLACE WITH FINAL COLLECTION


if USER_CREATE_NEW:
    try:
        # //> [ 3 ]DUMMY USER DATA FOR TESTING PURPOSES
        USER_FACE_DATA = {
            "user_id": "user909",
            "name": CLASS_NAMES[0],
            "account": "Tigers_IX",
            "position": "CEO",
            "email": "robbie_trevor@trax.io",
            "embedding": _ENCONDE_[0].tolist()
        }

        # //> INSERTS A RECORD FOR NEW OBJECT
        FACES_COLLECTION.insert_one(USER_FACE_DATA)
    except Exception as e:
        print(e)

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