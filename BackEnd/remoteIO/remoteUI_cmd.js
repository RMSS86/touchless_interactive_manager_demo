var zmq = require("zeromq");

exports.CMD_SUB_python = () => {
  const subscriber = zmq.socket("sub");

  subscriber.subscribe("");

  subscriber.on("message", function (message) {
    try {
      console.log(message);
      var message_ = JSON.parse(message);
      const CMD_ = message_["_CMD"];
      console.log("work: %s", message_);
      console.log("work: %s", CMD_);
      return CMD_; //do stuff
    } catch (e) {
      console.log("error " + e);
    }
  });

  subscriber.connect("tcp://127.0.0.1:5555");
  //subscriber.connect('tcp://127.0.0.1:8002');
  console.log("subscriber connected to port 5555");
  console.log("receiving messages...");
};

//module.exports = CMD_SUB_python;
