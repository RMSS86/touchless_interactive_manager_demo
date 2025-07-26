# from _CAMERA_ import _VIDEO_
# from  _TIM_MAIN_ import _App_
# test = 'here'
#
# _MA_ = _App_()
# _VD_ = _VIDEO_()
#
# if __name__ == "__main__":
#     step_one= _MA_._NX__router_IN_(test)
#     step_two = _MA_._NX__router_OUT_(step_one)
#     print('output to _CAMERA_',step_two)

####Inter server test###
# from _COMM_REQ_front_ import _PUB_react

_comm={
       'TYPE': 'CMD',
       '_CMD':'ZERO_'
}

# _PUB_react._SendCOMMAND_(_comm)

# server.py
import time
import zmq
import json
HOST = '127.0.0.1'
PORT = '5555'
_context = zmq.Context()
_publisher = _context.socket(zmq.PUB)
url = 'tcp://{}:{}'.format(HOST, PORT)

def publish_message(_message):
    try:
        _publisher.bind(url)
        time.sleep(0.6)
        _indented = json.dumps(_message,indent = 4)
        _sendMessageJson =json.loads(_indented)
        print(type(_sendMessageJson))
        _publisher.send_json(_sendMessageJson)

    except Exception as e:
        print('error: ', e)
    finally:
        _publisher.unbind(url)


publish_message(_comm)


