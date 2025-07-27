///////////////////////////////////////////////////////IMPORTS
//////////////////////////////////////////////////////////////
const express = require('express');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const mongoSanitize = require('express-mongo-sanitize');
const { xss } = require('express-xss-sanitizer');
const hpp = require('hpp');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const cors = require('cors');
const path = require('path');
const AppError = require('./utils/appError');
const globalErrorHandler = require('./controllers/errorController');
const tourRouter = require('./routes/tourRoutes'); 
const userRouter = require('./routes/userRoutes');
const reviewRouter = require('./routes/reviewRoutes');
const bookingRouter = require('./routes/bookingRoutes');
const viewRouter = require('./routes/viewRoutes'); 
///////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//> SAFE SAVE FOR RELOAD HERE! >>>  
///////////////////////////////////////////////////APP CREATION
///////////////////////////////////////////////////////////////
const app = express();
////////////////////////////////////////////////////TRUST PROXY
// app.enable('trust proxy');
//////////////////////////////////////////////GLOBAL MIDDLEWARES
/////////////////////////////////////////////CORS IMPLEMENTATION
app.use(
  cors({
    origin: 'http://localhost:3000',
    credentials: true,
  }),
);

app.options('*', cors());
// app.options('/api/v1/tours/:id', cors());
///////////////////////////////////////////////////////////////
////////////////////////////////////////////DEVELOPMENT LOGGING
if (process.env.NODE_ENV === 'development') {
  app.use(morgan('dev')); 
}
  
/////////////////////////////////////////////GLOBAL MIDDLEWARES
///////////////////////////////////////////////SET HTTP HEADERS
app.use(helmet()); 
// app.use(
//   helmet.contentSecurityPolicy({
//     directives: {
//       defaultSrc: ["'self'", 'https:', 'http:', 'data:', 'ws:'],
//       baseUri: ["'self'"],
//       fontSrc: ["'self'", 'https:', 'http:', 'data:'],
//       scriptSrc: ["'self'", 'https:', 'http:', 'blob:'],
//       styleSrc: ["'self'", "'unsafe-inline'", 'https:', 'http:'],
//     },
//   })
// );

/////////////////////////////////////////LIMIT REQUESTS FROM API
////////////////////////////////////////////////////////////////
const limiter = rateLimit({
  max: 100,
  windowMs: 60 * 60 * 1000,
  message: 'Too many requests from this IP, <please try again in an hour!>',
});
app.use('/api', limiter);
///1000 REQUESTS ON ROUTE API FROM IP ADDRESS, MANAGE IF NEEDED FOR MORE.
/////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////STRIPE MIDDLEWARE
///STRIPE WEBHOOK, BEFORE BODY-PARSER. STRIPE NEEDTHE BODY AS STREAM
////////////////////////////////////////////////////////////////////
// app.post(
//   '/webhook-checkout',
//   bodyParser.raw({ type: 'application/json' }),
//   bookingController.webhookCheckout
// );

//////////////BODY PARSER, READING DATA FROM BODY INTO [ req.body ]
///////////////////////////////////////////////////////////////////
app.use(bodyParser.json({ limit: '10kb' })); ///////LIMITS BODY SIZE
app.use(bodyParser.urlencoded({ extended: true, limit: '10kb' }));
app.use(cookieParser()); /////PARSES THE COOKIE DATA FROM FRONTEND
app.use(mongoSanitize()); ///DATA SANITATION> NOSQL QUERY INJECTION
app.use(xss()); ///////////////////////DATA SANITIZATION AGAIST XSS

////////////////////////////////////////PREVENT PARAMETER POLLUTION
///////////////////////////////////////////////////////////////////
app.use(
  hpp({
    whitelist: [
      'duration',
      'ratingsQuantity',
      'ratingsAverage',
      'maxGroupSize',
      'difficulty',
      'price',
    ],
  }),
);

///////////////////////////////////////////////////////////////
////////////////////////////////////////// SERVING STATIC FILES
///////////////////////////////////////////////////////////////
app.use(express.static(path.join(__dirname, 'public')));
///////////////////////////////////////////////////////////////
////////////////////////////////////////////MONITOR MIDDLEWARES
///////////////////////////////////////////////////////////////
app.use((req, res, next) => {
  console.log('[ MIDDLEWARE STACK RUNNING ]');
  next();
});

app.use((req, res, next) => {
  req.requestTime = new Date().toISOString();
  console.log(req.cookies);
  next();
});

/////////////////////////////////////////////////////////ROUTES
///////////////////////////////////////////////////////////////
app.use('/api/v1/views', viewRouter);
app.use('/api/v1/tours', tourRouter);
app.use('/api/v1/users', userRouter);
app.use('/api/v1/reviews', reviewRouter);
app.use('/api/v1/bookings', bookingRouter);
///////////////////////////////////////////////////////////////

////////////////////////////////////////////////////ERROR ROUTE
///////////////////////////////////////////////////////////////
app.all('*', (req, res, next) => {
  next(new AppError(`Can't find ${req.originalUrl} on this server!`, 404));
});

///////////////////////////////////////////////////ERROR HANDLE
///////////////////////////////////////////////////////////////
app.use(globalErrorHandler);
///////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////
module.exports = app; //////////////////////////////APP EXPORT
///////////////////////////////////////////////////////////////
