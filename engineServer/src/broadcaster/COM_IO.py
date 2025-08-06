import requests

from src.navigator.NAVIGATOR import NAVIGATOR


class COMM_IO:
    def __init__(self):
        self.CMD_PRE_OUT = None
        self.val = True
        self.cmd_ = 'CMD' # //> 4 TYPES OF COMMANDS
        self.urlCOMM = 'http://127.0.0.1:3001/usercmd/'


    def universal_COMM_Receiver_(self, __value, __handiness, __mode, __cmd_type, _log=True):

        match __handiness:
            # TODO //> ADD ACTION VAR ON self.CMD_compouser TO SELECT THE INTERNAL ACTION FILTRED BY CASE!

            case 'LEFT':
                match __mode:
                    case 'DIGITS':
                        # TODO: make a function for every __mode type
                        self.CMD_compouser(__value, 'LEFT', 'DIGITS', __cmd_type)

                    case 'CMDS':
                        self.CMD_compouser(__value, 'LEFT', 'CMDS', __cmd_type)

                    case 'AUTO_MOUSE':
                        self.CMD_compouser(__value, 'LEFT', 'AUTO_MOUSE', __cmd_type)

                    case 'FACE_REC':
                        self.CMD_compouser(__value, 'LEFT', 'FACE_REC', __cmd_type)

            case 'RIGHT':
                match __mode:
                    case 'DIGITS':
                        self.CMD_compouser(__value, 'RIGHT', 'DIGITS', __cmd_type)

                    case 'CMDS':
                        self.CMD_compouser(__value, 'RIGHT', 'CMDS', __cmd_type)

                    case 'AUTO_MOUSE':
                        self.CMD_compouser(__value, 'RIGHT', 'AUTO_MOUSE', __cmd_type)

                    case 'FACE_REC':
                        self.CMD_compouser(__value, 'RIGHT', 'FACE_REC', __cmd_type)


    # //> COMPOSES A JSON LIKE STRUCTURED MASSAGE
    def CMD_compouser(self, __value, __hand, __mode, __cmd_type, _log=False):

        # //> RECEIVES INPUTTED LONG COMMAND RECEIVED
        if __cmd_type == 'SHORT':

            if _log:
                print('[ {} ] FROM THE universal_COMM_Receiver_: MODE [ {} {} ]'.format(__value, __mode, 'SHORT'))

            # //> RECEIVES STRING FROM _COMPOSER_ AND MAKES IT A JSON FORMAT
            self.CMD_PRE_OUT = {'CMD_TYPE': 'SHORT',
                                'MODE': __mode,
                                'HANDNESS': __hand,
                                'VALUE': __value,
                                }

            self._CMD_SEND_(self.CMD_PRE_OUT, True ,False)
            # self.match_CMD(__value, __hand, __action ) # TODO: TAKE ACTIONS BASED ON LOGICAL TREE __action

        # //> RECEIVES INPUTTED LONG COMMAND RECEIVED
        if __cmd_type == 'LONG':

            if _log: #  __value, __hand, __mode, __cmd_type
                print('[ {} ] FROM THE universal_COMM_Receiver_: MODE [ {} {} ]'.format(__value, __mode, 'LONG'))


            # //> RECEIVES STRING FROM _COMPOSER_ AND MAKES IT A JSON FORMAT
            self.CMD_PRE_OUT =  {   'CMD_TYPE': 'LONG',
                                    'MODE': __mode,
                                    'HANDNESS': __hand,
                                    'VALUE': __value,

                                 }

            self._CMD_SEND_(self.CMD_PRE_OUT, True, False)
            # self.match_CMD(__value, __hand, __action ) # TODO: TAKE ACTIONS BASED ON LOGICAL TREE __action


    # //> [ ! ]SEND MESSAGE TO IO AND RETURNS STATUS CODE
    def _CMD_SEND_(self, __MSG, __send_cmd, __log=False):
         return self._sendCOMMAND_(__MSG, __send_cmd, __log)


    # //> SENDING COMMAND TO [ FE ] ON SOCKET.IO MODULE
    def _sendCOMMAND_(self, _comm, __send_cmd=True, __log=False):

        if __send_cmd:
            try: # //> STATES TO SEND REQUEST TO SOCKET.IO SERVER

                _req = requests.post(self.urlCOMM, data=_comm)
                req_ = _req.json()

                if __log:
                    #//> print('COMPOSED MESSAGE PREVIEW [ {} ]'.format(_comm))
                    self.logger(_comm, _req.status_code, req_)

                return _req.status_code


            except requests.exceptions.RequestException as e:
                print('ERROR SENDING MESSAGE: ', e)
                return -1
        else:
            if __log:
                print('COMPOSED MESSAGE PREVIEW [ {} ]'.format(_comm))
                return None
            return None

    # //> CONSOLE LOG RESULT OF FETCH /  SEND COMMAND
    def logger(self, _com, _status, __cmd):
        print('DATA SENT TO [ CD ] {}'
              ' \nSTATUS CODE [ {} ] \n:: RESPONSE {}'
              .format(_com, _status, __cmd))


    def match_CMD(self, __value, __handiness, __action):
        # //> TODO: FROM HERE DETERMINE THE TYPE OF ACCTION THE APP SHOULD DO LIKE MODE CHANGE, PAGE CHANGE ETC
        # //> COMMANDS WILL COME ALSO FROM UI IN RESPONSE OF THE UI STATE LOGIC
        # NAVIGATOR().route_selector('R1')

        match __action:

            case 'GET_TO_DIGITS_MODE':
                # NAVIGATOR().route_selector('R1')
                print('GETTING TO [ {} ] MODE'.format(__action))

            case 'GET_TO_CMDS_MODE':
                # NAVIGATOR().route_selector('R2')
                print('GETTING TO [ {} ] MODE'.format(__action))

            case 'GET_TO_DIGITS_MODE':
                # NAVIGATOR().route_selector('R3')
                print('GETTING TO [ {} ] MODE'.format(__action))

            case 'GET_AUTO_MOUSE_MODE':
                # NAVIGATOR().route_selector('R4')
                print('GETTING TO [ {} ] MODE'.format(__action))

            case 'GET_FACE_RECOGNITION_MODE':
                # NAVIGATOR().route_selector('R5')
                print('GETTING TO [ {} ] MODE'.format(__action))

            case 'OK_MENU_DISPLAY':
                print('GETTING [ {} ] DISLAYES'.format(__action))

            case _:  # //> UN-IMPLEMENTED CASE
                print('NOT IMPLEMENTED ENTRY')

    # TODO: SEND COMMAND FROM HERE USING COMMAND BUILDER TO [ FE ]
    # TODO: ACTIVE LISTEN TO LONG COMMANDS ACTIONS AND CHANGE MODE WITH NAVIGATOR

_NAV_ = NAVIGATOR()
