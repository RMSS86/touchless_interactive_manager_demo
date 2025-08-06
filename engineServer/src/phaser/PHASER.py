from src.broadcaster.COM_IO import COMM_IO
from collections import Counter

class PHASER:
    def __init__(self, __speed='normal',_log=True):

        # //> GLOBAL VARIABLES
        self.count_of_ = None
        self.value__ = None
        self.count__ = None
        self.count_of = None
        self.value_ = None
        self.count_ = None
        self._log = _log
        self.long_select_value = 3
        self.long_select_CMD = None

        # //> BUFFER COUNT VARIABLES
        self.tag_hand_command_ = []
        self.tag_hand_command_BH = []
        self.tag_mouse_command_ = []
        self.long_count = []
        self.long_count__ = []

        # //> DETERMINES SPEED BY INCREASING OR RECREASING SLOT SIZE
        if __speed == 'normal':
            self.slot_capacity = 21
        if __speed == 'fast':
            self.slot_capacity = 15

    # //> MAKES A COMMUNICATION DEVICE FOR COUNTING COMMANDS
    # //> MAKE FOR SINGLE HAND MODE DIGITS [ SINGLE-HAND ]AND DECODES COMMAND
    def Hand_CMD_Counter(self, _count, __handiness, __mode):
        self.tag_hand_command_.append(_count)
        self.CMD_normalizer(self.tag_hand_command_, __handiness, self.slot_capacity, __mode, False)

    # //> MAKES A COMMUNICATION DEVICE FOR COUNTING COMMANDS
    # //> MAKE FOR BOTH HANDS MODE RECOG HANDS AND DECODES COMMANDS
    def BH_CMD_Counter(self, _count, __handiness):
        self.tag_hand_command_BH.append(_count)
        self.CMD_normalizer(self.tag_hand_command_BH, __handiness, self.slot_capacity, "CMDS", False)

    # //> MAKES A COMMUNICATION DEVICE FOR COUNTING COMMANDS
    # //> MAKE FOR AUTO-MOUSE MODE HANDS AND DECODES OK_MENU COMMAND ONLY
    def Mause_CMD_counter(self, _count, __handiness, __mode, __speed=3):
        self.tag_mouse_command_.append(_count)
        self.CMD_normalizer(self.tag_mouse_command_, __handiness, __speed, __mode, False)

    # //> COMMANDER FUNCTIONS
    # //> NORMALIZER GETS DIFFERENT COUNTS TIMES INTO SINGLE CMD OR LONG PRESSED CMD
    # //< WITH LOCAL PRIVATE VARIABLES AND 2 THREADS SENDS SHORTED CMDS TO [_COMM_.universal_COMM_Receiver_]
    def CMD_normalizer(self, __command, __handiness, __slot_len, __mode, _log):
        if len(__command) == __slot_len: # //> BUFFER SIZE MET?
            counter__ = Counter(__command) # //> GET BUFFER ANALYSIS
            _value__, __count_of_ = counter__.most_common()[0]

            if _log:
                print('FROM HAND [ {} ] INCOMING COMMAND RECEIVED: [ {} ]'.format(__handiness, _value__))

            # //< PRIVATE THREAD FOR SENDING SHORTED CMDS TO [_COMM_.universal_COMM_Receiver_]
            _COMM_.universal_COMM_Receiver_(_value__, __handiness, __mode, 'SHORT', _log=self._log)
            # //< PRIVATE THREAD FOR SENDING LONG PRESSED CMDS TO  [self.CMD_listener]
            self.CMD_listener(_value__, __handiness, __mode)

            # //> WHEN MODE REACHED SHORT LIMIT RESET COUNTS
            if __mode == 'DIGITS' or 'AUTO_MOUSE': # //> THESE 2 ARE USED ONE AT TIME
                self.counter_reset()
            if __mode == 'CMDS':
                self.counter_reset_BH()


    # //> PARALLEL PROCESS FOR DETECTING LONG PRESSED CMS[WHEN RECEIVED BY self.long_select_value TIMES]
    def CMD_listener(self, value__, __handiness, __mode):
        self.long_count.append(value__)
        if len(Counter(self.long_count)) == 1:

            if len(self.long_count) == self.long_select_value: #//> BUFFER SIZE MET?
                self.long_count__ = Counter(self.long_count) # //> GET BUFFER ANALYSIS
                # //> THE Counter FUNCTION GETS ELEMENTS DISTRIBUTION BY NATURES / COUNT
                _value__, _count_of_ = self.long_count__.most_common()[0] # //< VALUES FOR LOGICAL USE
                _COMM_.universal_COMM_Receiver_(value__, __handiness, __mode, 'LONG', _log=self._log)
                # //> LONG COUNT RESET TO START ANOTHER CYCLE
                self.long_counter_reset()

        else:
            self.long_counter_reset()


    # //> GETS THE COMMAND FORM AUTO_MOUSE MODULE AND
    def Auto_Mouse_Manager(self, __cmd, __handiness):

        if __cmd == 'CLICK':
            # TODO: MAKE COMMAND SEND TO [ FE ] ANNOUNCING CLICK ACTION
            print('CLICKED!')  # NORMAL CLICK FUNCTION

        if __cmd == 'OK_MENU':
            # //> SEND OK COMMAND DOWN TO [ FE ]
            self.Mause_CMD_counter(__cmd, __handiness, "AUTO_MOUSE",3)


    # //> SHORT COUNT RESET
    def counter_reset(self):
        self.tag_hand_command_ = []
        self.tag_mouse_command_ = []

    # //> LONG COUNT RESET
    def long_counter_reset(self):
        self.long_count = []

    # //> DEDICATED SHORT COUNT RESET
    def counter_reset_BH(self):
        self.tag_hand_command_BH = []


_COMM_ = COMM_IO() # //> INVOKES UNIVERSAL COMMUNICATION MODULE
