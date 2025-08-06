const express = require("express");
const _app = express();
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");
const _Nx = require("./comdControllers/ioController");

_app.use(express.json());
_app.use(express.urlencoded({ extended: true }));

_app.use(cors());
const _server = http.createServer(_app);

//_app.use("api/v1/usercmd", cmdRouter);
_app.post("/", function (req, res) {
  const ipAddress = req.socket.remoteAddress;
  res.send(ipAddress);
});

_server.listen(3001, () => {
  console.log("server runnning port: [ 3001 ] ");
});

const sendCMD = (req, res, next) => {
  //CMD_ = req.params.cmd;
  RECEIVED_message_ = req.body;

  // var RECEIVED_message_ = JSON.parse(CMD_);
  // const _CMD = CMD_["_CMD"];

  // console.log('RECEIVED FROM sendCMD', RECEIVED_message_)

  try{
    //> GETS MESSAGE SENT TO FRONT END
    _Nx.sendCMD_(RECEIVED_message_);
  }
   
  catch(_){
   console.log('UNABLE_TO_SEND_TO_FRONTENDT')
  }

  res.status(200).json({
    command: 'RECEIVED FROM COMM_DEVICE',
  });
};

_app.post("/usercmd/", sendCMD);
//io.emit("userCMD_", CMD_);
