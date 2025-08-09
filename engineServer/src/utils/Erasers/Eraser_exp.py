import numpy as np
import cv2
import face_recognition

# //> IMPORTS ENV READERS
from dotenv import load_dotenv
from pathlib import Path

# //> IMPORTS MONGO CLOUDS DB CLASSES
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import os

# //> IMPORTS LOGICAL ML COMPARISON MODULE [ cosine_similarity ]
from sklearn.metrics.pairwise import cosine_similarity

# //> DEVELOPMENT VARS
DB_CONNECT = True
USER_CREATE_NEW = False

dotenv_path = '../../../../env/serverengine.env'

def DB_connect(__path, __db, __collection, __log=True):
    # //> [ 0 ]LOADS AN ENV FILE FROM RELATIVE PATH,
    _dotenv_path = Path(__path) # //< >>> USE[--env-file ]IN DOCKER
    load_dotenv(dotenv_path=_dotenv_path)

    # //> ACCESS ENVIRONMENT VARIABLES
    ES_DATABASE_RAW_CONN_STRING = os.getenv("ES_DATABASE")
    ES_MONGODB_USERNAME = os.getenv("ES_MONGODB_USERNAME")
    ES_MONGODB_PASSWORD = os.getenv("ES_MONGODB_PASSWORD")

    # //> [ 1 ]TARGET STRINGS IN ES_DATABASE_RAW_CONN_STRING TO REPLACE
    ES_TEMPLATE_USER = '<db_user>'
    ES_TEMPLATE_PWD = '<db_password>'

    # //> REPLACES TEMPLATE TARGET STRINGS FROM ES_DATABASE_RAW_CONN_STRING FOR AUTH CONNECTION TO SERVER
    ES_DATABASE_URL_CONN_STRING = ES_DATABASE_RAW_CONN_STRING.replace(ES_TEMPLATE_USER, ES_MONGODB_USERNAME).replace(ES_TEMPLATE_PWD, ES_MONGODB_PASSWORD)

    try: # //> SEND PING ON A SUCCESSFUL CONNECTION
        # //> CREATES A NEW CLIENT AND CONNECTS TO SERVER
        _MONGO_CLIENT = MongoClient(ES_DATABASE_URL_CONN_STRING, server_api=ServerApi('1'))
        # //> CONFIRMS THAT MONGO CLIENT HAD CREATED INSTANCE SUCCESSFULLY
        _MONGO_CLIENT.admin.command('ping')
        print("PING RESPONSE: CONNECTED TO MONGODB DATABASE")

        try:
            # //> [ 2 ]POINTER FOR SERVER DB AND COLLECTION
            DB_ = _MONGO_CLIENT[__db]  # //> REPLACE WITH FINAL DB
            _FACES_COLLECTION = DB_[__collection]  # //> REPLACE WITH FINAL COLLECTION
            # //> FETCHES ALL OBJECTS UNDER THE FACES_COLLECTION DB
            _STORED_FACES_ALL = list(_FACES_COLLECTION.find({}))
            # //> MAKES PARALLEL ARRAYS FOR STORED_EMBEDDINGS, STORED_NAMES
            _STORED_EMBEDDINGS = [doc['embedding'] for doc in _STORED_FACES_ALL]
            _STORED_NAMES = [doc['name'] for doc in _STORED_FACES_ALL]

            if __log:
                print('STORED_EMBEDDINGS {} \nSTORED_NAMES {}'.format(_STORED_EMBEDDINGS, _STORED_NAMES))

            return _FACES_COLLECTION, _STORED_EMBEDDINGS, _STORED_NAMES

        except Exception as e:
            print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))

    except Exception as e:
        print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))


# //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
RAW_IMG_SOURCE_PATH = '../data/faces/raw_images'

def face_embeddings(__face_loc='False', __cv=None, __dummy_name='John Doe', __log=False):
    if __face_loc != 'False':
        # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
        SOURCE_IMAGES = []
        CLASS_NAMES = []
        MYLIST = os.listdir(__face_loc)
        ENCODED_LIST = []

        for _cl in MYLIST:
            _RawImg = __cv.imread(f'{__face_loc}/{_cl}')
            # //> ENCODED IMAGES TO BE ENCODED BY BULK OR SINGLE SHOTS(THIS CASE)
            SOURCE_IMAGES.append(_RawImg)
            # //> CLEARS THE IMAGE NAME TO THE NAME NEED TO BE CHANGED IN EMP_ID
            CLASS_NAMES.append(os.path.splitext(_cl)[0])

        for _img in SOURCE_IMAGES:
            _img = __cv.cvtColor(_img, __cv.COLOR_BGR2RGB)

            _ENCODE = face_recognition.face_encodings(_img)[0]
            ENCODED_LIST.append(_ENCODE)

        if __log:
            print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(CLASS_NAMES, ENCODED_LIST[0].tolist()))

        return CLASS_NAMES, ENCODED_LIST[0].tolist()

    else: # //> FOR DUMMY TESTING PURPOSES GENERATED DATA
        # //> GENERAL FICTION NAME
        CLASS_NAMES = [__dummy_name]

        # //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
        ENCODED_LIST = np.random.rand(128).tolist()

        if __log:
            print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(CLASS_NAMES, ENCODED_LIST))

        return CLASS_NAMES, ENCODED_LIST


def get_similarity(__target, __records, __names, __log=False):
    # //> PERFORM SIMILARITY COMPARISON USING
    # [ scikit-learn's cosine_similarity ]

    if __records:
        # //> GETS THE PROXIMITY OPERATION
        similarities = cosine_similarity([__target], __records )[0]

        # FINDS THE MOST SIMILAR FACE
        most_similar_index = np.argmax(similarities)

        if similarities[most_similar_index] > 0.7:  # test threshold

            if __log:
                print(f"Identified as: {__names[most_similar_index]}") # //> SHOULD BE EMP ID

            return __names[most_similar_index]
        else:
            print("Face not recognized.")
    else:
        print("No faces stored in the database.")


# //> MAKES STRUCTURE FOR NEW ENTRY
def user_compouser(__name,
                   __embedding,
                   __id,
                   __account,
                   __position,
                   __email,
                   __log=False):

    # //> RETURNS JSON LIKE OBJECT
    return {
            "user_id": __id,
            "name": __name,
            "account":__account,
            "position":__position,
            "email":__email,
            "embedding": __embedding
        }


# //> MAKES INSERT FOR NEW ENTRY TO TARGET DATABASE
def insert_new_user(__user_data, __faces_collection, __log=False):

    try:
        # //> INSERTS A RECORD FOR NEW OBJECT
        __faces_collection.insert_one(__user_data)

        if __log:
            print("USER SUCCESSFULLY CREATED: {}".format(__user_data))

    except Exception as e:
        print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))


# //> [ 1.5 ]CREATION OF FACE DATA RAW_IMG_SOURCE_PATH,
# CLASS_NAMES, _ENCODE_ = face_embeddings(__face_loc=RAW_IMG_SOURCE_PATH, __cv=cv2, __log=True)

# # //> CONNECTS TO MONGODB SERVER
# FACES_COLLECTION, STORED_EMBEDDINGS, STORED_NAMES = DB_connect(dotenv_path, 'test','users')
#
# # //> PERFORMS CALCULATIONS COMPARING DISTANCES
# # //> ON IMPLEMENTATION, REMEMBER TO SET INPUT _ENCODE_ TO face_recognition.face_encodings(_img)[0] I/O
# get_similarity(_ENCODE_, STORED_EMBEDDINGS, STORED_NAMES, True) # //> _ENCODE_[0].tolist()
#

# //> IF REQUESTED
# if USER_CREATE_NEW:

# # //> CREATING NEW USER'S OBJECT
# NEW_USER_DATA = user_compouser('Robbie Stevenson', _ENCODE_,
#                                'user909', 'Tigers_IX', 'CEO',
#                                'robbie_trevor@trax.io')
#
# print(NEW_USER_DATA)
    # //> CREATING NEW USER'S RECORD
    # insert_new_user(NEW_USER_DATA, FACES_COLLECTION)

try:
    # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
    DB_SETTINGS_LOCAL_PATH = '../../database/database.env'

    # //> [ 0 ]LOADS AN ENV FILE FROM RELATIVE PATH,
    _dotenv_path = Path(DB_SETTINGS_LOCAL_PATH)
    load_dotenv(dotenv_path=_dotenv_path)

    # //> ONCE DATA IS COLLECTED
    _DB_ENV_PATH = os.getenv("DB_ENV_PATH")
    _DB = os.getenv("DB_NAME")
    _COLLECTION = os.getenv("DB_COLLECTION")
    print('DB SETTINGS LOADED FROM LOCAL ENV \n_DB_ENV_PATH [ {} ] \n_DB [ {} ] _COLLECTION [ {} ]'.format(_DB_ENV_PATH, _DB, _COLLECTION))

except Exception as e:
    # //> GENERICAL TEST DATABASE / COL
    _DB_ENV_PATH ='../../../env/serverengine.env'
    _DB = 'test'
    _COLLECTION = 'users'

    print('UNABLE TO FETCH DATA BROM LOCAL SETTING .ENV, ERROR: {} \n DEFAULT DATA LOADED TO DB_MANAGER INIT PROTOCOL'.format(e))
