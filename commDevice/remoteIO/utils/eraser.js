const express = require('express');
const _app = express();
const http = require('http');
const { Server } = require('socket.io');
const cors = require('cors');
//const _userCMD = require('./remoteUI_cmd');
const zmq = require('zeromq');

_app.use(cors());
const _server = http.createServer(_app);

const io = new Server(_server, {
  cors: {
    origin: 'http://localhost:3000',
    methods: ['GET', 'POST'],
  },
});

var message_CMD = _userCMD.CMD_SUB_python();

//var _CMD_ = JSON.parse(message_CMD);
console.log('Type of message_CMD', typeof message_CMD);

io.on('connection', (socket_) => {
  console.log(`user connected to ${socket_.id}`);
  //socket_.emit('userCMD_', message_CMD);
});
io.emit('userCMD_', message_CMD);
_server.listen(3001, () => {
  console.log('server runnning port 3001');
});
