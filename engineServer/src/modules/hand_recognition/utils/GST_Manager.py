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

            # //> TODO: IMPLEMENT PHASER
            self.command_history_L.appendleft(__CMD_I)
            if len(self.command_history_L) == self.history_length:
                self.mostCMMN_L = Counter(self.command_history_L).most_common()
                if __log:
                    print('右手が聞いた [ 索引 ]{}'.format(self.mostCMMN_L))
                # //> TODO: IMPLEMENT BROADCASTER CMD
                self.send_L = True
                self.command_history_L.clear()



        # //> _CHANNEL_ LISTENING TO THE RIGHT HAND [ MIGI-TE ]
        if __hander.classification[0].index == self.R_index:

            # //> TODO: IMPLEMENT PHASER
            self.command_history_R.appendleft(__CMD_I)
            if len(self.command_history_R) == self.history_length:
                self.mostCMMN_R = Counter(self.command_history_R).most_common()
                if __log:
                    print('右手が聞いた [ 索引 ]{}'.format(self.mostCMMN_R))
                # //> TODO: IMPLEMENT BROADCASTER CMD
                self.send_R = True
                self.command_history_R.clear()



        # //> EVALUATION MODE


    def Reset_Count(self):
        self.send_R = False
        self.send_L = False

# TODO: IMPORT PHASRR AND BRADCASTER, CREATE A COMMAND COMPOUSER MODEL AND THE APPS LIFECYCLE(HARDWRITTEN)