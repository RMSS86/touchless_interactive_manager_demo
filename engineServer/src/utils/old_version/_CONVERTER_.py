import cv2
from _TIM_MAIN_ import _App_

class _CONVERT_(object):
    def __init__(self):
        self.val =None

    def _get_frame_(self):
        self.jret, self.jpeg = cv2.imencode('.jpg', _MA_._NX__router_OUT_())
        return self.jpeg.tobytes()

_MA_=_App_()
