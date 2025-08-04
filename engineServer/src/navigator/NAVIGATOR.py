

class NAVIGATOR:
    def __init__(self):

        # //> COMMANDS BY NATURE ON THE APPS LIFE CYCLE
        self.routes =[{'R1': 'DIGITS', 'R2': 'CMDS',
                       'R3': 'FACE_REC', 'R4': 'AUTO-MOUSE',
                       'R5': 'SLEEP','R6': 'OFFLINE'}]

        self.route = None

        self.state = {
            '_state':'',
            '_status':'',
            '_com':'',
        }

    def nav_dictionary(self):
        pass

    def nav_remote(self, _com, _status, __cmd):
        self._com = _com
        self._status = _status
        self._cmd = __cmd

    # //> FUNCTION CHANGES VALUE OF ROUTE TO SWITCH DYNAMICALLY THE MODE
    def route_selector(self, __RX):
        self.route = self.routes[0][__RX]
        return self.route

