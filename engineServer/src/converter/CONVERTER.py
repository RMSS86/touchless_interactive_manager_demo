
class CONVERT(object):
    def __init__(self):
        self.val = None

    # //> GETS INCOMING SIGNAL AND CONVERTS TO JPG IMAGE(PER_SEC)
    def _get_frame_(self, __cv, __signal):
        self.jret, self.jpeg = __cv.imencode('.jpg', __signal)
        return self.jpeg.tobytes()

