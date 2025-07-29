

from flask import Flask, Response
from src.broadcaster.BROADCASTER import _BROADCASTER_
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
    return Response(_engine._framer(), mimetype='multipart/x-mixed-replace; boundary=frame')


class Engine:
    # //> CLASS VARIABLES DECLARATION
    def __init__(self, __mode=0, __squares=False, __rec=False, __hc=True):

        # //> GLOBAL CLASS VARIABLES
        self.fps_ = None
        self.bufferLen = 10

        # //> FRAMER CALCULATION FOR MODULES
        self.fps_ = FPS(buffer_len=self.bufferLen)
        self.recognition_active = __rec
        self.hand_command_active = __hc

    # //> FRAME GENERATOR / DATA INGESTION / PROCESSING
    def _framer(self):
        # //> MAIN LOOP INITIALIZER ### MAIN LOOP INITIALIZER ### MAIN LOOP INITIALIZER
        while _CAM_.active():  # //> CYCLES BEGIN ON _CAM_ isOPEN VALIDATOR
            self._fps = self.fps_.get()  # //> GETTING VAL FOR DRAWING INFO RATE
            self.key_frame = _CAM_.keyframe()  # //> SETTING GLOBAL KEY FRAMERS
            self._success, self._img = _CAM_.stream_()  # //< RAW  FEED FROM CAMERA CLASS self.debug_image

            if not self._success:
                break  # //> IF SOMETHING HAPPENS WITH WEBCAM LOOP WILL BREAK
            else:  # //< DYNAMIC MULTI MODULE STAGE WITH SAME VIDEO SIGNAL FLIP / RAW
                # //> BROADCASTING SIGNAL MODULE STAGE(CANVAS ONLY) ################################################## # //> SPLITSCREEN DYNAMIC MODULE EQUAL SIZE MODE
                yield _BROADCAST_._broadcaster(_CAM_.driver_(), self._img)  ####### //> PRE-BROADCASTING SIGNAL STAGE
                # //> BROADCASTING SIGNAL MODULE STAGE(CANVAS ONLY) ################################################# # //> SPLITSCREEN DYNAMIC MODULE EQUAL SIZE MODE


# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION
# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION
_CAM_ = Camera(0)  # //> PROMPTED CAMERA OBJECT WITH DEFAULT DEVICE TODO: MAKE IN DOCKER
_engine = Engine(1,False,True)  # //> MAIN APP BUILDER ENGINE
_BROADCAST_ = _BROADCASTER_()  # //> BROADCASTING TO SELF SERVER ENGINE
# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION
# //< MODULES AND CLASSES IMPORT AND SCOPE DECLARATION


# //> MAIN APPLICATION STARTER ## MAIN APPLICATION STARTER
if __name__ == '__main__': # //> MAIN APPLICATION STARTER
    app.run(host='0.0.0.0', port=5000, debug=False)
# //> MAIN APPLICATION STARTER ## MAIN APPLICATION STARTER



