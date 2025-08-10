#
# import cv2 as __cv
# from src.database.DB_MANAGER import DB_MANAGER
# from src.modules.face_recognition.FACE_EMBEDDINGS import FACE_EMBEDDINGS
#
# # //> INVOKE DB_MANAGER
# _DBM_ = DB_MANAGER()
# _FR_EMB_ = FACE_EMBEDDINGS()
# RAW_IMG_SOURCE_PATH = '../data/faces/raw_images'
#
# # //> [ 1.5 ]CREATION OF FACE DATA RAW_IMG_SOURCE_PATH,
# CLASS_NAMES, _ENCODE_ = _FR_EMB_.face_embeddings(RAW_IMG_SOURCE_PATH, __cv, False)
#
# print('FROM [ RAW_IMG_SOURCE_PATH ]:\nCLASS_NAMES {} \nEMBEDDINGS {}'.format(CLASS_NAMES, len(_ENCODE_)))
#
#
# # //> GET CURRENT DATABASE SETTINGS FROM ENV FILE
# _db, _collection = _DBM_.get_db_settings('../../database/database.env', False)
#

# # //> INSERT USER FROM DB BY ID[#NAME]
# _NEW_USER = _DBM_.user_compouser(_name=CLASS_NAMES[1],_id='id_4895',
#                        _account='TIGER_IX',
#                        _position='Supervisor',
#                        _email='siphia@trax.io',
#                        _embedding=_ENCODE_[1].tolist(),)
# print(_NEW_USER)
#
# #


#//> INSERT USER FROM DB BY ID[#NAME]
# _SAVED_NEW_USER = _DBM_.insert_new_user(_NEW_USER,True)


# # //> GET CURRENT DATABASE RECORDS FROM SERVER
# _FACES_COLLECTION, _STORED_EMBEDDINGS, _STORED_NAMES = _DBM_.fetch_whole_db_to_Local(_db, _collection, True)


# # //> FETCHING USER FORM DB BY ID[#NAME]
# _FETCHED_USER = _DBM_.fetch_single_user_by_ID('John Doe')
# print('FETCHED USER FROM SERVER::\n{}'.format(_FETCHED_USER))


# //> DELETING USER FROM DB BY ID[#NAME] John Doe
# _DBM_.delete_single_user_by_ID('John Doe')


# //> TODO: MAKE A RESPONSIVE SWITHCER THAT CHANGES MODE ON LONG COMMANDS



# //> TODO: GET THE USER DATABASE SIMILAR CRUD TO DUMMY USERS COLLECTION PRIOR TO >>>
# //< TODO: CREATE A REAL USERS DATABASE UNDER A USERS COLLECTION, THEN GET THE FACES EMBEDDINGS INTO
#  THE USER_EMBEDDINGS COLLECTION STORING EMBS, AND USER [_id] FROM [USERS] COLLECTION! MANAGED BY THE BACK END


