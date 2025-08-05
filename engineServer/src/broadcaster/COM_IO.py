import requests

class COMM_IO:
    def __init__(self):
        self.val = True
        self.cmd_ = 'CMD' # //> 4 TYPES OF COMMANDS
        self.urlCOMM = 'http://127.0.0.1:3001/usercmd/'


    def universal_COMM_Receiver_(self, __value, __handiness, __cmd_type):
        print('VALUE [ {} ] HAND [ {} ] TYPE [ {} ] FROM COMM_IO.universal_COMM_Receiver_'.format(__value, __handiness, __cmd_type))


    # //> RECEIVES STRING FROM _COMPOSER_ AND MAKES IT A JSON FORMAT
    def CMD_PRE_OUT_(self, __composed):
        return { self.cmd_ : __composed }


    # //> [ ! ]SEND MESSAGE TO IO AND RETURNS STATUS CODE
    def _CMD_SEND_(self, __MSG, __log=False):
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

    def match_CMD(self, __value, __handiness):

        match __value:
            case 'POINTER':
                print('LONG SELECTION DETECTED! {} HAND [ {} ]'.format(__handiness, __value))
            case 'OK_MENU':
                print('LONG SELECTION DETECTED! {} HAND [ {} ]'.format(__handiness, __value))

            case _:  # //> UN-IMPLEMENTED CASE
                print('NOT IMPLEMENTED ENTRY')

    # TODO: SEND COMMAND FROM HERE USING COMMAND BUILDER TO [ FE ]
    # TODO: ACTIVE LISTEN TO LONG COMMANDS ACTIONS AND CHANGE MODE WITH NAVIGATOR
