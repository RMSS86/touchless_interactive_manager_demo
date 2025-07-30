from collections import Counter

class PHASER:
    def __init__(self, __speed='normal'):
        self.count_of = None
        self.value_ = None
        self.count_ = None
        self.tag_hand_command_ = []

        if __speed == 'normal':
            self.slot_capacity = 16
        if __speed == 'fast':
            self.slot_capacity = 12

    def Hand_CMD_Counter(self, _count):
        self.tag_hand_command_.append(_count)

        if len(self.tag_hand_command_) == self.slot_capacity:
            self.count_ = Counter(self.tag_hand_command_)
            self.value_, self.count_of = self.count_.most_common()[0]
            # TODO: SEND COMMAND FROM HERE USING COMMAND BUILDER TO [ FE ]
            # _SW_._universal_COMM_Receiver_(self.tag_hand_command_[0])
            print(self.value_)
            self.counter_reset()

    def counter_reset(self):
        self.tag_hand_command_ = []



