import cv2

class _VIDEO_(object):
    def __init__(self, *args):
        self._capture_ = cv2.VideoCapture(0)

    def __del__(self):
        self._capture_.release()

    def _Stream_(self):
        self.ret, self.frame, = self._capture_.read()
        return self.ret, self.frame

