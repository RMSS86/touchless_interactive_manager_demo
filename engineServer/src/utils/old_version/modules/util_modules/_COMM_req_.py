import zmq
import json
###REQUEST MANAGER THAT ASK THE REQUESTO TO THE MINI SERVER REP!
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://127.0.0.1:5555')

sentMessage={
           'TYPE': 'CMD',
           '_CMD':'ZERO_'
}

sentMessageJson=json.dumps(sentMessage)
socket.send_json(sentMessageJson)

socket.close()
context.term()


# import zmq
# import json
# ###REQUEST MANAGER THAT ASK THE REQUESTO TO THE MINI SERVER REP!
# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect('tcp://127.0.0.1:5555')
#
# sentMessage={
#            'TYPE': 'CMD',
#            '_CMD':'ZERO_'
# }
#
# sentMessageJson=json.dumps(sentMessage)
# socket.send_json(sentMessageJson)
#
# socket.close()
# context.term()