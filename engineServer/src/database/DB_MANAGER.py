# //> IMPORTS ENV READERS
from dotenv import load_dotenv
from pathlib import Path

# //> IMPORTS MONGO CLOUDS DB CLASSES
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


class DB_MANAGER:
    def __init__(self, __path='database/database.env', __log=False): # '../../database/database.env'

        # //> GETS DB PUBLIC VARS
        self.DB_SETTINGS_LOCAL_PATH = None
        self._DB_ENV_PATH = None
        self._COLLECTION = None
        self._DB = None

        # //> UPDATING SETTINGS VARIABLES
        self.get_db_settings(__path, __log)

        # //> INITIAL VARIABLES
        self._STORED_NAMES = None
        self._STORED_EMBEDDINGS = None
        self._STORED_FACES_ALL = None
        self._FACES_COLLECTION = None
        self._MONGO_CLIENT = None
        self.ES_TEMPLATE_PWD = None
        self.ES_TEMPLATE_USER = None
        self._dotenv_path = None
        self.ES_MONGODB_PASSWORD = None
        self.ES_MONGODB_USERNAME = None
        self.ES_DATABASE_RAW_CONN_STRING = None
        self.ES_DATABASE_URL_CONN_STRING = None
        self.DB_ = None


        # //> INITIAL VARIABLES FOR CONSTRUCTING DATABASE API ENCORE
        self.FACES_COLLECTION, self.STORED_EMBEDDINGS, self.STORED_NAMES \
            = self.DB_connect(self._DB_ENV_PATH, self._DB, self._COLLECTION, __log )

    # //> CONNECTS INSTANCE TO MONGODB SERVER
    def DB_connect(self, __path, __db, __collection, __log=True):
            # //> [ 0 ]LOADS AN ENV FILE FROM RELATIVE PATH,
            self._dotenv_path = Path(__path)  # //< >>> USE[--env-file ]IN DOCKER
            load_dotenv(dotenv_path=self._dotenv_path)

            # //> ACCESS ENVIRONMENT VARIABLES
            self.ES_DATABASE_RAW_CONN_STRING = os.getenv("ES_DATABASE")
            self.ES_MONGODB_USERNAME = os.getenv("ES_MONGODB_USERNAME")
            self.ES_MONGODB_PASSWORD = os.getenv("ES_MONGODB_PASSWORD")

            # //> [ 1 ]TARGET STRINGS IN ES_DATABASE_RAW_CONN_STRING TO REPLACE
            self.ES_TEMPLATE_USER = '<db_user>'
            self.ES_TEMPLATE_PWD = '<db_password>'

            # //> REPLACES TEMPLATE TARGET STRINGS FROM ES_DATABASE_RAW_CONN_STRING FOR AUTH CONNECTION TO SERVER
            self.ES_DATABASE_URL_CONN_STRING = self.ES_DATABASE_RAW_CONN_STRING.replace(
                self.ES_TEMPLATE_USER, self.ES_MONGODB_USERNAME).replace(self.ES_TEMPLATE_PWD, self.ES_MONGODB_PASSWORD)

            try:
                # //> SEND PING ON A SUCCESSFUL CONNECTION
                # //> CREATES A NEW CLIENT AND CONNECTS TO SERVER
                self._MONGO_CLIENT = MongoClient(self.ES_DATABASE_URL_CONN_STRING, server_api=ServerApi('1'))

                # //> CONFIRMS THAT MONGO CLIENT HAD CREATED INSTANCE SUCCESSFULLY
                self._MONGO_CLIENT.admin.command('ping')
                print("PING RESPONSE: CONNECTED TO MONGODB DATABASE")

                # //> RETURNS DIRECTLY [ self._FACES_COLLECTION, self._STORED_EMBEDDINGS, self._STORED_NAMES ]
                return self.fetch_whole_db_to_Local(__db,__collection,True)

            except Exception as e:
                print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))
                return 'AN_UNEXPECTED_ERROR_OCCURRED'


    # //> MAKES STRUCTURE FOR NEW ENTRY
    def user_compouser(self, _name='',
                       _id='',
                       _account='',
                       _position='',
                       _email='',
                       _embedding='[128]',
                       __log=False):

        # //> RETURNS JSON LIKE OBJECT
        return {
                "user_id": _id,
                "name": _name,
                "account":_account,
                "position":_position,
                "email":_email,
                "embedding": _embedding
            }


    # //> GETS THE WHOLE DATABASE EMBEDDINGS AND ARRANGES TO TEMP LOCAL VAR
    def fetch_whole_db_to_Local(self, __db, __collection, __log=True):
        try:
            # //> [ 2 ]POINTER FOR SERVER DB AND COLLECTION
            self.DB_ = self._MONGO_CLIENT[__db]  # //> REPLACE WITH FINAL DB
            self._FACES_COLLECTION = self.DB_[__collection]  # //> REPLACE WITH FINAL COLLECTION
            # //> FETCHES ALL OBJECTS UNDER THE FACES_COLLECTION DB
            self._STORED_FACES_ALL = list(self._FACES_COLLECTION.find({}))
            # //> MAKES PARALLEL ARRAYS FOR STORED_EMBEDDINGS, STORED_NAMES
            self._STORED_EMBEDDINGS = [doc['embedding'] for doc in self._STORED_FACES_ALL]
            self._STORED_NAMES = [doc['name'] for doc in self._STORED_FACES_ALL]

            if __log:
                print('fetch_whole_db_to_Local \nSTORED_EMBEDDINGS [ {} ] \nSTORED_NAMES {}'.format(len(self._STORED_EMBEDDINGS), self._STORED_NAMES))

            return self._FACES_COLLECTION, self._STORED_EMBEDDINGS, self._STORED_NAMES

        except Exception as e:
            print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))
            return ['ERROR_WHILE_FETCHING']



    # //> FETCHES FROM .ENV LOCAL FILE DB SETTINGS DB, COLLECTION
    def get_db_settings(self, __path, __log=False):

        try:
            # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
            self.DB_SETTINGS_LOCAL_PATH = __path

            # //> [ 0 ]LOADS AN ENV FILE FROM RELATIVE PATH,
            _dotenv_path = Path(self.DB_SETTINGS_LOCAL_PATH)
            load_dotenv(dotenv_path=_dotenv_path)

            # //> ONCE DATA IS COLLECTED
            self._DB_ENV_PATH = os.getenv("DB_ENV_PATH")
            self._DB = os.getenv("DB_NAME")
            self._COLLECTION = os.getenv("DB_COLLECTION")


            if __log:
                print('DB SETTINGS LOADED FROM LOCAL ENV \n_DB_ENV_PATH [ {} ] \n_DB [ {} ] _COLLECTION [ {} ]'.format(
                    self._DB_ENV_PATH, self._DB, self._COLLECTION))

            return self._DB, self._COLLECTION # //< RETURNED VALUES FOR GENERIC USES

        except Exception as e:

            # //> GENERICAL TEST DATABASE / COL
            self._DB_ENV_PATH = '../../../env/serverengine.env'
            self._DB = 'test'
            self._COLLECTION = 'users'

            print(
                'UNABLE TO FETCH DATA fROM LOCAL SETTING .ENV, ERROR: {} '
                '\n DEFAULT DATA LOADED TO DB_MANAGER INIT PROTOCOL'.format(e))

            return 'UNABLE_TO_FETCH_DATA_FROM_LOCAL_SETTING_ENV'

    # //> MAKES INSERT FOR NEW ENTRY TO TARGET DATABASE
    def insert_new_user(self, __user_data, __log=False):

        try:
            # //> INSERTS A RECORD FOR NEW OBJECT
            self.FACES_COLLECTION.insert_one(__user_data)

            if __log:
                print("USER SUCCESSFULLY CREATED: {}".format(__user_data))

        except Exception as e:
            print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))


    # //> FETCHING USER FORM DB BY ID
    def fetch_single_user_by_ID(self, __id,__log=False):
        try:
            if __log:
                print('fetch_wholefetch_single_user_by_ID FROM [ {} ] FETCHING [ {} ]'.format(
                    self._FACES_COLLECTION, __id))

            # return self._FACES_COLLECTION.find_one({"_id": __id})
            return self._FACES_COLLECTION.find_one({"name": __id})

        except Exception as e:
            print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))
            return ['ERROR_WHILE_FETCHING']


    # //> FETCHING USER FORM DB BY ID
    def delete_single_user_by_ID(self, __id,__log=False):
        try:
            if __log:
                print('fetch_wholefetch_single_user_by_ID FROM [ {} ] DELETING [ {} ]'.format(
                    self._FACES_COLLECTION, __id))

            return self._FACES_COLLECTION.delete_one({"name": __id})

        except Exception as e:
            print('AN UNEXPECTED ERROR OCCURRED: {}'.format(e))
            return ['ERROR_WHILE_DELETING']

