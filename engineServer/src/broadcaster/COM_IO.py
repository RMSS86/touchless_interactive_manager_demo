import requests

class COMM_IO:
    def __init__(self):
        self.val = True
        self.cmd_ = 'CMD' # //> 4 TYPES OF COMMANDS
        self.urlCOMM = 'http://127.0.0.1:3001/usercmd/'


    def universal_COMM_Receiver_(self, __value, __handiness):
        print('VALUE [ {} ] HAND [ {} ] FROM COMM_IO'.format(__value, __handiness))


    # //> RECEIVES STRING FROM _COMPOSER_ AND MAKES IT A JSON FORMAT
    def CMD_PRE_OUT_(self, __composed):
        return { self.cmd_ : __composed }


    # //> [ ! ]SEND MESSAGE TO IO AND RETURNS STATUS CODE
    def _CMD_SEND_(self,__MSG, __log=False):
         return self._sendCOMMAND_(__MSG, __log)

    # //> SENDING COMMAND TO [ FE ] ON SOCKET.IO MODULE
    def _sendCOMMAND_(self, _comm, __log=False):

        try: # //> STATES TO SEND REQUEST TO SOCKET.IO SERVER
            _req = requests.post(self.urlCOMM, data=_comm)
            req_ = _req.json()

            if __log:
                self.logger(_comm, _req.status_code, req_['_CMD'])

            return _req.status_code

        except requests.exceptions.RequestException as e:
            print('ERROR SENDING MESSAGE: ', e)
            return -1

    # //> CONSOLE LOG RESULT OF FETCH /  SEND COMMAND
    def logger(self, _com, _status, __cmd):
        print('DATA SENT TO [ CD ] {}'
              ' \nSTATUS CODE [ {} ] \n:: RESPONSE {}'
              .format(_com, _status, __cmd))
