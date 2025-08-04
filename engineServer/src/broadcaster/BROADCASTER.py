from src.converter.CONVERTER import _CONVERT_
import requests

class _BROADCASTER_:
    def __init__(self):
        self.BRDCST_image = None

    # //> BROADCAST VIDEO SIGNAL ON DEMAND VIA IMG/SRC
    def _broadcaster(self, __driver, __signal):
        # //> ADDABLE ELEMENTS STAGE SUCH AS ON IMAGE QR CODE
        self.BRDCST_image = _CONVERT._get_frame_(__driver, __signal)

        # //> DECODES AND RETURN BROADCASTABLE SIGNAL
        return (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + self.BRDCST_image + b'\r\n\r\n')


_CONVERT = _CONVERT_()



