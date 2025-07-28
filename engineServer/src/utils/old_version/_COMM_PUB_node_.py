# server.py
import time
import zmq
import json


class _CMD_PUB_Node_():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = '5555'
        self._context = zmq.Context()
        self._publisher = self._context.socket(zmq.PUB)
        self.url = 'tcp://{}:{}'.format(self.HOST, self.PORT)

    def _SendCOMMAND_(self,_message):
        try:
            self._publisher.bind(self.url)
            time.sleep(0.3)
            self._indented = json.dumps(_message, indent=4)
            self._sendMessageJson = json.loads(self._indented)
            self._publisher.send_json(self._sendMessageJson)
            print(self._sendMessageJson )
        except Exception as e:
            print('error: ', e)
        finally:
            self._publisher.unbind(self.url)
