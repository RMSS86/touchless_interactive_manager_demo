

import requests

class _Broadcaster():
    def __init__(self):
        self.urlCOMM = 'http://127.0.0.1:3001/usercmd/'

    def _SendCOMMAND_(self, _comm):
        _req = requests.post(self.urlCOMM, data=_comm)
        print('data from the _SendCOMMAND_', _comm)
        print('response from commDevice', _req)
