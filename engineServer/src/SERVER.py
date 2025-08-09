from src.broadcaster.BROADCASTER import BROADCASTER
from src.navigator.NAVIGATOR import NAVIGATOR
from src.switcher.SWITCHER import SWITCHER

from flask import Flask, Response
from src.camera.CAMERA_ import Camera
from src.camera.FPS import FPS

# //> FLASK APP CREATION
app = Flask(__name__) # //> FLASK APP CREATION
# //> FLASK APP CREATION

# //< END POINTS DECLARATION FOR SELF NON-STATIC SERVER
# //< END POINTS DECLARATION FOR SELF NON-STATIC SERVER

# //> VIDEO STREAMING ENDPOINT(DECODED)
@app.route('/video_feed')
def video_feed():
    return Response(engine_.framer_(), mimetype='multipart/x-mixed-replace; boundary=frame', status=200)

# //< END POINTS DECLARATION FOR SELF NON-STATIC SERVER
# //< END POINTS DECLARATION FOR SELF NON-STATIC SERVER
ROUTE = 'R4'

# //> ENGINE INIT
class Engine:
    # //> CLASS VARIABLES DECLARATION
    def __init__(self, __mode=0, __squares=False, __rec=False, __hc=True):
        # //> GLOBAL CLASS VARIABLES
        self._success = None
        self.key_frame = None
        self._fps = None
        self.fps_ = None
        self.handsNumber = 1
        self.keyframeLen = 10
        self.bufferLen = 10
        self.historyLen = 16
        self._img = None
        self.debug_image = None
        self.debugged_image_OUT = None
        self.min_dtc_conf = 0.5
        self.padding_framer = 18
        self.ingestion_index = None

        # //> DATA INGESTION MODE SPECIFICS
        self.recordingColor = (245, 117, 16)
        self.waitColor = (16, 117, 245)
        self.min_dtc_conf = 0.5
        self.waitKey = 1000

        # //> FRAMER CALCULATION FOR MODULES
        self.fps_ = FPS(buffer_len=self.bufferLen)
        self.recognition_active = __rec
        self.hand_command_active = __hc

    # //> FRAME GENERATOR / DATA INGESTION / PROCESSING
    def framer_(self):

        # //> MAIN LOOP INITIALIZER
        while _CAM_.active(): # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR

        # //> TODO: ROUTER KEY FOR PASSING DOWN TO _SW_.router
            self._fps = self.fps_.get() # //> GETTING VAL FOR DRAWING INFO RATE
            self.key_frame = _CAM_.keyframe() # //> SETTING GLOBAL KEY FRAMERS
            self._success, self._img = _CAM_.stream_() # //< RAW  FEED FROM CAMERA CLASS self.debug_image

            if not self._success: # //> IF ENGINE RUNS SUCCESSFULLY THEN >>>
                break  # //> IF SOMETHING HAPPENS WITH WEBCAM LOOP WILL BREAK

            else: # //< DYNAMIC MULTI MODULE STAGE WITH SAME VIDEO SIGNAL FLIPPED / RAW / IN-SERIES
                self._img = _SW_.router(_CAM_, self._img, self._success) # //< [ MODES MIDDLEWARE ROUTER AREA ]

                # //> BROADCASTING SIGNAL MODULE STAGE(CANVAS ONLY) //> SPLITSCREEN DYNAMIC MODULE EQUAL SIZE MODE
                yield _BROADCAST_.broadcaster_(_CAM_.driver_(), self._img) # //> PRE-BROADCASTING SIGNAL STAGE
                # //> BROADCASTING SIGNAL MODULE STAGE(CANVAS ONLY)  //> SPLITSCREEN DYNAMIC MODULE EQUAL SIZE MODE

# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION
# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION

_BROADCAST_ = BROADCASTER()  # //> BROADCASTING TO SELF SERVER ENGINE
_CAM_ = Camera(0)  # //> PROMPTED CAMERA OBJECT WITH DEFAULT DEVICE
engine_ = Engine(1,False,True,True)  # //> MAIN APP BUILDER ENGINE
_SW_ = SWITCHER('R1') # //> GLOBAL ROUTER OPERATES WITH NAVIGATOR
# _NAV_ = NAVIGATOR('R4') # //> GLOBAL ROUTER OPERATES WITH SWITCHER
# //> GLOBAL ROUTER ENGINE FOR PROCESSED IMAGE FUNCTIONS BACK TO BROADCASTER

# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION
# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION

# //> MAIN APPLICATION STARTER ## MAIN APPLICATION STARTER
if __name__ == '__main__': # //> MAIN APPLICATION STARTER
    app.run(host='0.0.0.0', port=5000, debug=False)
# //> MAIN APPLICATION STARTER ## MAIN APPLICATION STARTER



# TODO: NAVIGATOR MUST GO ON THIS TOP LEVEL AND PASS DOWN THE ROUTE VALUE