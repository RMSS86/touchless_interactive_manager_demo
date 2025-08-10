import numpy as np
import face_recognition
import cv2

# //> SYSTEM MODULE
from datetime import datetime
import os

class FACE_EMBEDDINGS:
    def __init__(self):
        # //> [ PRE ]TAKE REAL BIOMETRICS FROM PICTURED RESOURCES
        self._ENCODE = None
        self._RawImg = None
        self.MYLIST = None
        self.SOURCE_IMAGES = []
        self.CLASS_NAMES = []
        self.ENCODED_LIST = []
        
    # //> GETS LOCAL DATA FOTO FOR INGESTION> EMBEDDING DATA / NAME(USER_ID)
    def face_embeddings(self, __face_loc='FAKE_DATA', __log=False):
        if __face_loc != 'FAKE_DATA':

            self.MYLIST = os.listdir(__face_loc)
            
            for _cl in self.MYLIST:
                self._RawImg = cv2.imread(f'{__face_loc}/{_cl}')
                # //> ENCODED IMAGES TO BE ENCODED BY BULK OR SINGLE SHOTS(THIS CASE)
                self.SOURCE_IMAGES.append(self._RawImg)
                # //> CLEARS THE IMAGE NAME TO THE NAME NEED TO BE CHANGED IN EMP_ID
                self.CLASS_NAMES.append(os.path.splitext(_cl)[0])

            for _img in self.SOURCE_IMAGES:
                _img = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB)

                self._ENCODE = face_recognition.face_encodings(_img)[0]
                self.ENCODED_LIST.append(self._ENCODE)

            if __log:
                print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES,
                                                                            self.ENCODED_LIST)) # [0].tolist()
            # //> RETURNS NORMALIZED VALUES
            return self.CLASS_NAMES, self.ENCODED_LIST #[0].tolist()

        if __face_loc == 'FAKE_DATA':  # //> FOR DUMMY TESTING PURPOSES GENERATED DATA
            # //> GENERAL FICTION NAME
            self.CLASS_NAMES = ['John Doe']

            # //> [ XTRA ]EXAMPLE OF FACE_EMBEDDING (REPLACE WITH DATA FROM face_recognition) AFTER TEST
            self.ENCODED_LIST = np.random.rand(128).tolist()

            if __log:
                print('FROM face_embeddings NAMES, EMBEDDINGS {} {}'.format(self.CLASS_NAMES, self.ENCODED_LIST))

            return self.CLASS_NAMES, self.ENCODED_LIST
        return None
