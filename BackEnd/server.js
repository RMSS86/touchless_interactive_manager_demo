const mongoose = require('mongoose');
const dotenv = require('dotenv');
const app = require('./app');

///ENV vars for when not using Docker
dotenv.config({ path: '../env/backend.env' });

process.on('uncaughtException', (err) => {
  console.log('UNCAUGHT EXCEPTION! [ Shutting down ]');
  console.log(err.name, err.message);
  process.exit(1);
});

const _port = process.env.PORT || 80;
const _DB = process.env.DATABASE.replace(
  '<db_user>',
  process.env.MONGODB_USERNAME,
).replace('<db_password>', process.env.MONGODB_PASSWORD);

mongoose
  .connect(_DB)
  .then(() => {
    console.log('[ CONNECTED TO MONGODB ]');
    console.log(`APP RUNNING [ ON PORT: ${_port} ]`);
    const server = app.listen(_port);
  })
  .catch((err) => {
    console.error('[ FAILED TO CONNECT TO MONGODB ]');
    console.error(err);
  });

process.on('unhandledRejection', (err) => {
  console.log('UNHANDLED REJECTION!  [ Shutting down ]');
  console.log(err.name, err.message);
  server.close(() => {
    process.exit(1);
  });
});
