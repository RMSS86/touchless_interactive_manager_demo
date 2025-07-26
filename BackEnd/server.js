const mongoose = require('mongoose');
const dotenv = require('dotenv');



process.on('uncaughtException', err => {
    console.log('UNCAUGHT EXCEPTION! 💥 Shutting down...');
    console.log(err.name, err.message);
    process.exit(1);
  });

dotenv.config({ path: '../config.env' });
const app = require('./app');//APP importing

const _PORT = process.env.SERVER_PORT || 80;
_DB= `mongodb+srv://${process.env.MONGODB_USERNAME}:${process.env.MONGODB_PASSWORD}@${process.env.MONGODB_URL}/TIMV1?retryWrites=true&w=majority`

mongoose.connect(
    _DB,
    {
      useNewUrlParser: true,
      useUnifiedTopology: true
    }).then(() => {
      // console.log(con.connections);
      console.log('DB connection Succesful!');
    });

const server = app.listen(_PORT, () => {
  console.log(`App running on port ${_PORT}...`);
});


process.on('unhandledRejection', err => {
  console.log('UNHANDLED REJECTION! :: Shutting down...');
  console.log(err.name, err.message);
  server.close(() => {
    process.exit(1);
  });
});

