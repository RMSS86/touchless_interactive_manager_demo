import cv2 as _cv
import copy

from src.camera.ARGS_init_ import ArgsInit


class Camera(object):
    def __init__(self, __mode=0):
        # //> CREATING DEVICE ARGS
        self.mode = __mode
        _args = Args.get_args()
        _cap_device = _args.device
        _cap_width = _args.width
        _cap_height = _args.height
        self.KEYFRAME = None

        # //> CREATING SIGNAL VARIABLES
        self._img = None
        self.debug_image = None
        self.ret = None
        self.frame = None

        # //> CREATING CAMERA DEVICE
        self._capture_ = _cv.VideoCapture(_cap_device)  # //> MAIN CAMERA DEVICE CREATION
        self._capture_.set(_cv.CAP_PROP_FRAME_WIDTH, _cap_width)  # //> DEVICE INPUT WIDTH
        self._capture_.set(_cv.CAP_PROP_FRAME_HEIGHT, _cap_height)  # //> DEVICE INPUT HEIGHT

    def stream_(self, _key_frames_rate=10):
        self.KEYFRAME = _key_frames_rate
        _cv.waitKey(self.KEYFRAME)

        if self.mode==0: # //> FOR CLEAN FOR HOLISTIC DRAWING
            self.ret, self.frame = self._capture_.read()
            self._img = _cv.flip(self.frame, 1)  # //> MIRRORING DISP
            return self.ret, self._img

        if self.mode==1: # //>  FOR RAW MANUAL BRECT DRAWING
            self.ret, self.frame = self._capture_.read()
            self._img = _cv.flip(self.frame, 1)  # //> MIRRORING DISP
            self.debug_image = copy.deepcopy(self._img)  # //> THE BROADCASTER CANVAS SIGNAL
            self._img = _cv.cvtColor(self._img, _cv.COLOR_BGR2RGB) # //> THE PROCESSING RAW SIGNAL
            return self.ret, self._img, self.debug_image

        if self.mode==2: # //> FOR HYBRID DRAWING
            self.ret, self.frame = self._capture_.read()
            self._img = _cv.flip(self.frame, 1)  # //> MIRRORING DISP
            self.debug_image = copy.deepcopy(self._img)  # //> THE BROADCASTER CANVAS SIGNAL
            return self.ret, self._img, self.debug_image
        return None

    def driver_(self):
        return _cv

    def active(self):
        return self._capture_.isOpened()

    def keyframe(self):
        return self.KEYFRAME

    def __del__(self):
        self._capture_.release()  # //> CASH REMOVE ON STOP
        _cv.destroyAllWindows()  # //> WINDOWS REMOVE ON STOP

Args = ArgsInit()  # //> INITIAL ARGUMENTS SET
