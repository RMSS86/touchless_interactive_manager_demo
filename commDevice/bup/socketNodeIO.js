const express = require("express");
const _app = express();
const http = require("http");
const { Server } = require("socket.io");
const cors = require("cors");
//const _userCMD = require('./remoteUI_cmd');
const zmq = require("zeromq");

_app.use(cors());
const _server = http.createServer(_app);

const io = new Server(_server, {
  cors: {
    origin: [
      "http://localhost:3000",
      "http://localhost:3001",
      "http://localhost:5000",
    ],
    methods: ["GET", "POST"],
  },
});

const CMD_SUB_python = () => {
  const subscriber = zmq.socket("sub");
  subscriber.subscribe("");

  subscriber.on("message", function (message) {
    try {
      //console.log(typeof message);
      var message_ = JSON.parse(message);
      console.log(message_);
      console.log(typeof message_);
      const CMD_ = message_["_CMD"];
      console.log(typeof CMD_);
      //console.log('work: %s', message_);
      console.log("work: %s", CMD_);
      io.emit("userCMD_", CMD_);
      return CMD_;
      //do stuff
      //return message_;
    } catch (e) {
      console.log("error " + e);
    }
  });

  subscriber.connect("tcp://127.0.0.1:5555");
  //subscriber.connect('tcp://127.0.0.1:8002');
  console.log("subscriber connected to port 5555");
  console.log("receiving messages...");
};

io.on("connection", (socket_) => {
  console.log(`user connected to ${socket_.id}`);
  //socket_.emit('userCMD_', message_CMD);
  CMD_SUB_python();
});

_server.listen(3001, () => {
  console.log("server runnning port 3001");
});
