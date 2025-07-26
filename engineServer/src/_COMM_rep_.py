import zmq
###MINI SERVER!
class ZMQ_REP_():
    def __init__(self):
        self.dir_= 'tcp://127.0.0.1:5555'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(self.dir_)

    def _COMM_(self):
        self.message = self.socket.recv_json()
        print('Message received %s' % self.message)

        self.socket.close()
        self.context.term()

ZMQ_REP_()._COMM_()

# import zmq
# ###MINI SERVER!
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind('tcp://127.0.0.1:5555')
#
# message = socket.recv_json()
# print('Message received %s' % message)
#
# socket.close()
# context.term()
