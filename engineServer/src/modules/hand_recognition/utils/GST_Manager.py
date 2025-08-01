from collections import Counter
from collections import deque


class GST_MANAGER_:
    def __init__(self):
        self.active = True
        self.L_index = 0
        self.R_index = 1
        self.send_L = False
        self.send_R = False

        self.history_length = 16
        self.mostCMMN_L = None
        self.mostCMMN_R = None
        self.current_CMD_ = None

        self.point_history = deque(maxlen=self.history_length)
        self.command_history_L = deque(maxlen=self.history_length)
        self.command_history_R = deque(maxlen=self.history_length)

    def _handedness_(self, __hander, __CMD_I, __log=False):

        # //> _CHANNEL_ LISTENING TO THE LEFT HAND [ HIDARI-TE ]
        if __hander.classification[0].index == self.L_index:
            self.command_history_L.appendleft(__CMD_I)
            if len(self.command_history_L) == self.history_length:
                self.mostCMMN_L = Counter(self.command_history_L).most_common()
                self.send_L = True
                self.command_history_L.clear()

            if __log:
                print('左手が聞いた [ 索引 ]{ ', __hander.classification[0].index, ' }')

        # //> _CHANNEL_ LISTENING TO THE RIGHT HAND [ MIGI-TE ]
        if __hander.classification[0].index == self.R_index:
            self.command_history_R.appendleft(__CMD_I)
            if len(self.command_history_R) == self.history_length:
                self.mostCMMN_R = Counter(self.command_history_R).most_common()
                self.send_R = True
                self.command_history_R.clear()

            if __log:
                print('右手が聞いた [ 索引 ]{ ', __hander.classification[0].index, ' }')

        # //> EVALUATION MODE
        if self.send_L and self.send_R:
            print(f'Command Combo [L-R] {self.mostCMMN_L} : {self.mostCMMN_R}')
            # self.Vocoder(_INTRP_.interpreter_(self.mostCMMN_L[0][0], self.mostCMMN_R[0][0]))
            self.Reset_Count()



    def Reset_Count(self):
        self.send_R = False
        self.send_L = False

