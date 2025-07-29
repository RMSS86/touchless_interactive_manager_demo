
class _CONVERT_(object):
    def __init__(self):
        self.val = None

    def _get_frame_(self, __cv, __signal):
        self.jret, self.jpeg = __cv.imencode('.jpg', __signal)
        return self.jpeg.tobytes()

