from _COMM_PUB_node_ import _CMD_PUB_Node_
# from _COMM_IO_ import _CMD_ON_Node_
from _COMM_IO_ import _Broadcaster

#TODO:  this is the main work flow managr, operatas validations, menu flow, rules and modes.
class _NAVIGATOR_():
    def __init__(self,*args, **kwargs):
        self.menu = {'1': 'SELECT', '2': 'ACCEPT', '3': 'CANCEL', '4': 'BACK', '5': 'MENU'}  # Change to BINARY


    def _to_Client_COMMD(self, _comm):
        print(_comm, ' FROM THE NAVIGATOR!!')
        _BR_._SendCOMMAND_(_comm)
        # _CMD_react_._SendCOMMAND_(_comm)
        #_CMD_frontend_._SendCOMMAND_(_comm)
        #_BR_.emit(event='_user_cv2CMD', data=_comm)
        #TODO: re factor rotor rectangle functionality

# _CMD_react_ =_CMD_PUB_Node_()
#_CMD_frontend_=_CMD_ON_Node_()
_BR_=_Broadcaster()