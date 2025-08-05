from src.broadcaster.COM_IO import COMM_IO
from collections import Counter

class PHASER:
    def __init__(self, __speed='normal',_log=True):
        self.count_of_ = None
        self.value__ = None
        self.count__ = None
        self.count_of = None
        self.value_ = None
        self.count_ = None
        self._log = _log
        self.long_select_value = 3
        self.long_select_CMD = None

        self.tag_hand_command_ = []
        self.tag_hand_command_BH = []
        self.tag_mouse_command_ = []
        self.long_count = []
        self.long_count__ = []


        if __speed == 'normal':
            self.slot_capacity = 16
        if __speed == 'fast':
            self.slot_capacity = 12

    def Hand_CMD_Counter(self, _count, __handiness, __mode):
        self.tag_hand_command_.append(_count)
        self.CMD_normalizer(self.tag_hand_command_, __handiness, self.slot_capacity, __mode, False)


    def BH_CMD_Counter(self, _count, __handiness):
        self.tag_hand_command_BH.append(_count)
        self.CMD_normalizer(self.tag_hand_command_BH, __handiness, self.slot_capacity, "CMDS", False)


    def Mause_CMD_counter(self, _count, __handiness, __mode, __speed=3):
        self.tag_mouse_command_.append(_count)
        self.CMD_normalizer(self.tag_mouse_command_, __handiness, __speed, __mode, False)


    def CMD_normalizer(self, __command, __handiness, __slot_len, __mode, _log):
        if len(__command) == __slot_len:
            counter__ = Counter(__command)
            _value__, __count_of_ = counter__.most_common()[0]

            if _log:
                print('FROM HAND [ {} ] INCOMING COMMAND RECEIVED: [ {} ]'.format(__handiness, _value__))

            _COMM_.universal_COMM_Receiver_(_value__, __handiness, __mode, 'SHORT')
            self.CMD_listener(_value__, __handiness, __mode)

            if __mode == 'DIGITS' or 'AUTO-MOUSE':
                self.counter_reset()
            if __mode == 'CMDS':
                self.counter_reset_BH()


    def CMD_listener(self, value__, __handiness, __mode):
        self.long_count.append(value__)
        if len(self.long_count) == self.long_select_value:
            self.long_count__ = Counter(self.long_count)

            _value__, _count_of_ = self.long_count__.most_common()[0]
            _COMM_.universal_COMM_Receiver_(value__, __handiness, __mode, 'LONG')

            self.long_counter_reset()


    def Auto_Mouse_Manager(self, __cmd, __handiness):

        if __cmd == 'CLICK':
            # TODO: MAKE COMMAND SEND TO [ FE ] ANNOUNCING CLICK ACTION
            print('CLICKED!')  # NORMAL CLICK FUNCTION


        if __cmd == 'OK_MENU':
            # //> SEND OK COMMAND DOWN TO [ FE ]
            self.Mause_CMD_counter(__cmd, __handiness, "AUTO-MOUSE",4)




    def counter_reset(self):
        self.tag_hand_command_ = []
        self.tag_mouse_command_ = []

    def long_counter_reset(self):
        self.long_count = []

    def counter_reset_BH(self):
        self.tag_hand_command_BH = []


_COMM_ = COMM_IO()
