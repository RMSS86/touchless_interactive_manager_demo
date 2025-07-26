const express = require("express");
const app_ = express();
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");

app_.use(cors());
const server_ = http.createServer(app_);
const _io = new Server(server_, {
  cors: {
    origin: [
      "http://localhost:3000",
      "http://localhost:3001",
      "http://localhost:5000",
    ],
    methods: ["GET", "POST"],
  },
});

_io.on("connection", (socket_) => {
  console.log(`user connected to ${socket_.id}`);
  //socket_.emit('userCMD_', message_CMD);
});

server_.listen(3002, () => {
  console.log("server runnning port: [ 3002 ] ");
});

exports.sendCMD_ = (cmd) => {
  console.log("from the 3002 server: ", cmd);
  _io.emit("userCMD_", cmd);
};
