import io from "socket.io-client";
const _socket = io.connect("http://localhost:3002");

export default _socket;
