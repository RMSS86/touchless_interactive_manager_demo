# import socketio
#
# sio = socketio.Client()
# message={
#             "TYPE": "CMD",
#             "_CMD": "ONE_"
#         }
# @sio.event
# def connect():
#     print('connection established')
#     sio.emit(event='_user_cv2CMD', data=message)
#
# @sio.event
# def my_message(data):
#     # print('message received with ', data)
#     sio.emit(event='_user_cv2CMD', data=data)
#
# @sio.event
# def disconnect():
#     print('disconnected from server')
#
# sio.connect('http://localhost:3001')
# sio.wait()

# from socketIO_client import SocketIO
# from socketIO_client.transports import TRANSPORTS
import sys

message={
            "TYPE": "CMD",
            "_CMD": "ONE_"
        }


import socketio
class Broadcaster(object):
    port = 3001
    host = "http://localhost:"

    def __init__(self, port=3001, host="http://localhost:"):
        self.port = port
        self.host = host
        self.socketIO = socketio.Client(engineio_logger=True, logger=True)
        self.address_ = "%s%s" %(self.host,str(self.port))
        print(self.address_)
        self.message={
            "TYPE": "CMD",
            "_CMD": "ONE_"
        }
        try:
            self.socketIO.connect(self.address_)
            print('server running on %s' % (self.address_))
        except Exception as e:
            print(e)


        #self.socketIO.on("ack", self.logACK)

    def logACK(self, data):
        print("Acknowledgement received for %s" % data['original'])


    def emit(self, event, data):
        self.socketIO.emit(event, data)
        print(data)
        self.wait_forever()

    def on(self, event, callback):
        self.socketIO.on(event, callback)

    def wait(self, millis):
        self.socketIO.wait(millis)

    def wait_forever(self):
        self.socketIO.wait()

    def messageReceiver(self,_data):
        print(_data)

# _BR_=Broadcaster()
# _BR_.emit(event='_user_cv2CMD', data=_BR_.message)

#TODO: if erro persists, make aPI call to the commdevice end with CMD, the command can ba passed of to front end :).

