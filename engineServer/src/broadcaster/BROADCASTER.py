from src.converter.CONVERTER import _CONVERT_
import requests


class _BROADCASTER_:
    def __init__(self):
        self.val = True
        self.BRDCST_image = None
        self.urlCOMM = 'http://127.0.0.1:3001/usercmd/'

    # //> BROADCAST VIDEO SIGNAL ON DEMAND VIA IMG/SRC
    def _broadcaster(self, __driver, __signal):
        # ADDABLE ELEMENTS STAGE SUCH AS ON IMAGE QR CODE
        self.BRDCST_image = _CONVERT._get_frame_(__driver, __signal)
        return (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + self.BRDCST_image + b'\r\n\r\n')

    def _sendCOMMAND_(self, _comm, __log=False):
        try:
            _req = requests.post(self.urlCOMM, data=_comm)
            req_ = _req.json()
            if __log:
                print('DATA SENT TO [ CD ] {} '
                      '\nSTATUS CODE [ {} ] '
                      '\n:: RESPONSE {}'.format(_comm, _req.status_code, req_['_CMD']))
            return _req.status_code

        except requests.exceptions.RequestException as e:
            print('ERROR SENDING MESSAGE: ', e)
            return -1


_CONVERT = _CONVERT_()
