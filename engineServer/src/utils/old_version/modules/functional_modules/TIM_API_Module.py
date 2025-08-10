import numpy as np
import asyncio
#import pymongo
# DataFrames / dataBase Connection Modules
from sqlalchemy import create_engine

class UD_API():
    def __init__(self, **kwargs):
        ###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###
        ###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###

        ###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###
        ###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###SQL-DB_CREDENTIALS###
        self.connection_string = "MONGO CONNECTION STRING HERE"

    def _CONN_SQL(self):
        #####SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR#####
        #####SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR#####
        self.DATABASE_CONNECTION = f'mssql://{self.USERNAME}:{self.PASSWORD}@{self.SERVER}/{self.DATABASE}?driver={self.DRIVER}'
        self.engine = create_engine(self.DATABASE_CONNECTION, execution_options={'stream_results': True})
        self.connection = self.engine.connect()
        return self.connection
        #####SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR#####
        #####SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR###SQL-DB_CONNECTOR#####

    def _CONN_MONGO(self):
        #####MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR#####
        #####MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR#####
        pass
        ####MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR#####
        #####MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR###MONGO-DB_CONNECTOR#####

    def _CONN(self):
        # self.client =pymongo.MongoClient(self.connection_string, )
        # self.MongoDataBase = client["TIM_Manager"]
        # self.MongoCollection =database["facial_database"]
        pass


    def _bridge_(self, current_frame=None, encoded_frame=None):
    ####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL DATABASE####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL /FBS DATABASE###
    ####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL DATABASE####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL /FBS DATABASE###

        try: ####SAFE CODE ON INITIAL STATE####
            if current_frame and encoded_frame == None:
                print('INITIALIZING: [ current_frame, encoded_frame ]')

        except Exception as err:
            print(err)

        try:
            ####TRANSLATING LOCATIONS AND ENCODERS TO BE SPLITTED AND CLEANED PRIOR API CALL###
            self.current_frame_, self.encoded_frame_raw = current_frame, encoded_frame
            ####TRANSLATING LOCATIONS AND ENCODERS TO BE SPLITTED AND CLEANED PRIOR API CALL###

            ####ASYNC FUNCTION FOR API AUTO CALL####ASYNC FUNCTION FOR API AUTO CALL####ASYNC FUNCTION FOR API AUTO CALL
            asyncio.run(self.API_Splitter(encoders=self.encoded_frame_raw,facelocs=self.current_frame_))#[0]
            ####ASYNC FUNCTION FOR API AUTO CALL####ASYNC FUNCTION FOR API AUTO CALL####ASYNC FUNCTION FOR API AUTO CALL

        # TODO: self.encoded_frame_raw lock for one per at time, len < 1 send alert(ON A MODE MANAGER IN OPTIONS)!
        except Exception as err:
            print(err)

    ####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL DATABASE####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL /FBS DATABASE###
    ####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL DATABASE####NEXUS BETWEEN FACIAL ROTOR & MONGO/ SQL /FBS DATABASE###

    async def API_Splitter(self, encoders, facelocs):
    ####GETS THE NUMBER FACES FROM FACIAL ROTOR FOR MAKING AN API CALL INDIVIDUALLY(WHEN ALLOWED!)
    ####GETS THE NUMBER FACES FROM FACIAL ROTOR FOR MAKING AN API CALL INDIVIDUALLY(WHEN ALLOWED!)

        ####STEP #1: CONVERTING ARRAYS INTO LIST:
        self.arg_lenght = int(len(encoders))
        self.raw_ueclidean_coors = []

        for n in range(self.arg_lenght):
            self.encs = []
            for i in encoders[n]:
                self.encs.append(i)
            self.raw_ueclidean_coors.append(self.encs)
        await self._DIAL_TASK_driver(self.raw_ueclidean_coors)

    #TODO: ####STEP #2:SERVING THE FACE LOCATIONS FOR USAGE pre & AFTER DIALER:

    async def _DIAL_TASK_driver(self, list: list):
        self.single_enc = False
        self.inc_obj_len = int(len(list))

        print('ARRANGE LENGHT: ', self.inc_obj_len)
        print('LENGHT OF THE CLEANED OBJECT OF LISTS: ', list)
        #####ASSESMENT FOR SINGLE PERSON VS SENTINEL MODE#####
        if len(list) == 1:
            self.single_enc = True
        else:
            self.single_enc = False
        #####ASSESMENT FOR SINGLE PERSON VS SENTINEL MODE#####
        try:
            self.TASKS = [self.AUTO_MONGO_Dialer(list[COUNT]) for COUNT in range(self.inc_obj_len)]
            self.RESULT = await asyncio.gather(*self.TASKS, return_exceptions=True)
        except Exception as err:
            print(err)

    async def AUTO_MONGO_Dialer(self, ud_arg):
        print('TASK STARTED')
        #await asyncio.sleep(1.0)
        self.UD_ARG()
        print('FROM MONGO AUTO DIALER: ', ud_arg)
        print('TASK DONE')
        # self.UD_ARG(response)

    async def UD_ARG(self, *args):
        await asyncio.sleep(5.4)
        pass
    #TODO: this returns value _UNKOWN_ if false or object jason object with agents info if true with values, this will connecto with the SWITCHER for puting in yellow the recognition box on a api call?
    #TODO: send API call Get to backEnd and declares in the mean time the fetching yellow tag on agent face.
