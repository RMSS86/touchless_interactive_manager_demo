from collections import Counter

class PHASER:
    def __init__(self, __speed='normal',_log=True):
        self.count_of = None
        self.value_ = None
        self.count_ = None
        self._log = _log

        self.tag_hand_command_ = []
        self.tag_hand_command_BH = []

        if __speed == 'normal':
            self.slot_capacity = 16
        if __speed == 'fast':
            self.slot_capacity = 12

    def Hand_CMD_Counter(self, _count): # _handness
        self.tag_hand_command_.append(_count)

        if len(self.tag_hand_command_) == self.slot_capacity:
            self.count_ = Counter(self.tag_hand_command_)
            self.value_, self.count_of = self.count_.most_common()[0]

            # TODO: SEND COMMAND FROM HERE USING COMMAND BUILDER TO [ FE ]
            # _SW_._universal_COMM_Receiver_(self.tag_hand_command_[0])

            if self._log:
                print('INCOMING COMMAND RECEIVED: [ {} ]'.format(self.value_))

            self.counter_reset()

    def BH_CMD_Counter(self, _count, _handness):
        self.handiness_BH = _handness.classification[0].label.upper()
        self.tag_hand_command_BH.append(_count)

        if len(self.tag_hand_command_BH) == self.slot_capacity:
            self.count_BH = Counter(self.tag_hand_command_BH)
            self.value_BH, self.count_of_BH = self.count_BH.most_common()[0]

            # TODO: SEND COMMAND FROM HERE USING COMMAND BUILDER TO [ FE ]
            # _SW_._universal_COMM_Receiver_(self.tag_hand_command_[0])

            if self._log:
                print('FROM HAND [ {} ] INCOMING COMMAND RECEIVED: [ {} ]'.format(self.handiness_BH, self.value_BH))

            self.counter_reset_BH()

    def Auto_Mouse_Manager(self, __cmd):

        if __cmd == 'CLICK':
            # TODO: MAKE COMMAND SEND TO [ FE ] ANNOUNCING CLICK ACTION
            print('CLICKED!')  # NORMAL CLICK FUNCTION
            pass

        if __cmd == 'OK_MENU':
            # //> SEND OK COMMAND DOWN TO [ FE ]
            self.Hand_CMD_Counter(__cmd)
            pass


    def counter_reset(self):
        self.tag_hand_command_ = []

    def counter_reset_BH(self):
        self.tag_hand_command_BH = []



