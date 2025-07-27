const mongoose = require('mongoose');
const fs = require('fs');
const Tour = require('./../../models/tourModel');
const Review = require('./../../models/reviewModel');
const User = require('./../../models/userModel');

const _DB = process.env.DATABASE.replace('<db_user>',process.env.MONGODB_USERNAME).replace('<db_password>',process.env.MONGODB_PASSWORD);

mongoose
  .connect(_DB, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useFindAndModify: false
  })
  .then(() => console.log('DB CONNECTION SUCCESSFUL'));

  const tours = JSON.parse(fs.readFileSync(`${__dirname}/tours.json`, 'utf-8'));
    const users = JSON.parse(fs.readFileSync(`${__dirname}/users.json`, 'utf-8'));
    const reviews = JSON.parse(fs.readFileSync(`${__dirname}/reviews.json`, 'utf-8'));
  
  // IMPORT DATA INTO DB
  const importData = async () => {
    try {
      await Tour.create(tours);
      await User.create(users, { validateBeforeSave: false });
    await Review.create(reviews);
      console.log('Data successfully loaded!');
    } catch (err) {
      console.log(err);
    }
    process.exit();
  };
  
  // DELETE ALL DATA FROM DB
  const deleteData = async () => {
    try {
      await Tour.deleteMany();
      await User.deleteMany();
      await Review.deleteMany();
      console.log('Data successfully deleted!');
    } catch (err) {
      console.log(err);
    }
    process.exit();
  };
  
  if (process.argv[2] === '--import') {
    importData();
  } else if (process.argv[2] === '--delete') {
    deleteData();
  }