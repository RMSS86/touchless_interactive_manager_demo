/////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR//////
/////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR//////
// const DUMMY_TOUR = {description: 
//     "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
//     difficulty: "easy",
//     duration: 5,
//     durationWeeks: 0.7142857142857143,
//     guides: [],
//     id: "5c88fa8cf4afda39709c2951",
//     imageCover
//     : 
//     "trax-7.jpg",
//     images
//     : 
//     (3) ['tour-1-1.jpg', 'tour-1-2.jpg', 'tour-1-3.jpg'],
//     locations
//     : 
//     (3) [{…}, {…}, {…}],
//     maxGroupSize
//     : 
//     25,
//     name
//     : 
//     "The Forest Hiker",
//     price
//     : 
//     397,
//     ratingsAverage,
//     : 
//     5,
//     ratingsQuantity,
//     : 
//     9,
//     reviews,
//     : 
//     [],
//     secretTour,
//     : 
//     false,
//     slug
//     : 
//     "the-forest-hiker",
//     startDates
//     : 
//     (3) ['2021-04-25T09:00:00.000Z', '2021-07-20T09:00:00.000Z', '2021-10-05T09:00:00.000Z'],
//     startLocation
//     : 
//     {type: 'Point', coordinates: Array(2), description: 'Banff, CAN', address: '224 Banff Ave, Banff, AB, Canada'},
//     summary
//     : 
//     "Breathtaking hike through the Canadian Banff National Park and more.",
//     trending
//     : 
//     true
//     __v
//     : 
//     0
//     _id
//     : 
//     "5c88fa8cf4afda39709c2951"};
/////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR//////
/////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR////DUMMY_TOUR//////

/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////
/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////
const DUMMY_TOUR = {}
const DUMMY_USER = {
  _id: {
    $oid: "6791a462e993cb015ba65339",
  },
  role: "user",
  active: true,
  name: "Trevor R. Stevenson",
  email: "scottsland14@trax.io",
  password: "$2b$12$Rf0EYU729u7xte5ST8OrXOogLWtF6UoGxJtOFzljqJ9hJJ5DNPwou",
  __v: 0,
  passwordChangedAt: {
    $date: "2025-03-18T23:56:27.895Z",
  },
};
/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////
/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////DUMMY_USER/////

/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////
/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////
const DUMMY_REVIEW = {
  _id: {
    $oid: "67955bb748b1e803b34dd364",
  },
  rating: 4.5,
  review: "Basically the best tour ever being in!",
  tour: {
    $oid: "67954fb0a7e7e8021f7a9a4f",
  },
  user: {
    $oid: "67941c922dc42e01794d3c2a",
  },
  createdAt: {
    $date: "2025-01-25T21:46:31.680Z",
  },
  __v: 0,
};

/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////
/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////DUMMY_REVIEW/////
export { DUMMY_TOUR, DUMMY_USER, DUMMY_REVIEW };

///.\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
