

class FACE_RECOGNITION:
    def __init__(self):
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        self.CATEGORIES = ['Load Entries']
        self.INITIAL_LISTS = ['Load Entries']
        self.array_dims = 128

        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        ####VAR_FOR_QUERIES####VAR_FOR_QUERIES####VAR_FOR_QUERIES####
        self.user_ID = '2'
        self._index_ = 0

        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        self._tag_counter_= []

        self.tag_NameColor = (255, 255, 255)  # RGB for White
        self.square_Not_Color = (112, 112, 246)  # RGB for Red
        self.square_Fetching_Color = (230, 226, 109)  # RGB for Yellow
        self.square_Match_Color = (0, 255, 0)  # RGB for Green

        self._nameTagFailed = '_UNKNOWN_'
        self._nameTagFetching = '_FETCHING_'

        self._square_tag_factor = 4
        self._square_text_factor = 6

        self._eval_pharser_factor = 3
        self._eval_pharser_factor_fail= 3

        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        ###INDEX ON FACE RECOGNITION INSTRUCTION MAP###INDEX ON FACE RECOGNITION INSTRUCTION MAP###
        ###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE
        self.COMMS = ['MOUSE', 'COUNT']
        self.bridge = self.COMMS[0]
        ###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE###SWITCHER ALLOWARE

        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        self.path = 'utils/Sources/Images/AttendingPeople'
        self.SourceImages = []
        self.ClassNames = []
        self.myList = os.listdir(self.path)  # Sets the path on disc for the images to take please before mounting.
        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        ###OVerwrite one Euclidean distances MOdule ready in SQL DataBase.
        #(TO BE FIXED WITH MONGO OR POSGREsql IMPLEMENTATION!)