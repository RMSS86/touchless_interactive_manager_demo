const mongoose = require('mongoose');
const slugify = require('slugify');

// const { trim } = require('validator');
// const User = require('./userModel');

/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

const Schema = mongoose.Schema;
const tourSchema = new Schema({

name: {
  type: String,
  required: [true, 'A Tour must have a Name'], 
  unique: true, 
  trim: true,
  maxlength: [40, 'A tour name must have less or equal then 40 characters'],
  minlength: [10, 'A tour name must have more or equal then 10 characters']
  // validate: [validator.isAlpha, 'Tour name must only contain characters']
},

slug: String,

duration: {
  type: Number,
  required: [true, 'A Tour must hacve a Duration in time:Minutes']
},

maxGroupSize: {
  type: Number,
  required: [true, 'A Tour Must have a Gruop Size']
},

difficulty: {
  type: String, 
  required: [true,'A Tour Must have a Difficulty level' ],
  enum: {
    values: ['easy', 'medium', 'difficult', "Expert"],
    message: 'Difficulty is either: easy, medium, difficult or expert'
  }
},

ratingsAverage: {
  type: Number,
  default: 4.5,
  min: [1, 'Rating must be above 1.0'],
  max: [5, 'Rating must be below 5.0'],
  set: val => Math.round(val * 10) / 10 // 4.666666, 46.6666, 47, 4.7
},

ratingsQuantity: {
  type: Number,
  default: 0,
},

price: {
  type: Number,
  required: [true, 'A Tour must have Price'], 
},

priceDiscount: {
  type: Number,
  validate: {
    validator: function(val) {
      // this only points to current doc on NEW document creation
      return val < this.price;
    },
    message: 'Discount price ({VALUE}) should be below regular price'
  }
},

summary:{
  type: String,
  trim: true,
  required: [true, 'A Tour must have a Summary']
},

description:{
  type: String,
  trim: true 
},

imageCover:{
  type: String,
  required: [true, 'A Tuour Must have a Image Cover']
},

images: [
  String
],

createdAt:{
type:Date,
default: Date.now(),
select: false
},

startDates: [
  Date
],

secretTour: {
  type: Boolean,
  default: false
},

trending:{
  type: Boolean,
  default: false
},
startLocation:{
  //GEOJSON
  type: {
    type: String,
    default: 'Point',
    enum: ['Point']
  },
  coordinates: [ Number ],
  address: String,
  description: String
},
locations:[
  {
    type:{
      type: String,
      default: 'Point',
      enum: ['Point']
    },
    coordinates: [ Number ],
    address: String,
    description: String,
    day: Number
  }
],
////GUIDES
guides: [
    {
      type: mongoose.Schema.ObjectId,
      ref:'User',
    }
],
/////ADD
},
{
  toJSON: { virtuals: true },
  toObject: { virtuals: true }
});


/////////////////////////////////////////////////////////////////////////
///EMBEDING THE GUDIES TO TOURS USING PROMISES(APPLY FOR MULTI ARRAY REALTED FIELDS)
///FOR SAVING NOT FOR UPDATING INFO! EMBEDING
// tourSchema.pre('save', async function(next){
//   const guidesPromises = this.guides.map(async id => await User.findById(id));
//   this.guides = await Promise.all(guidesPromises);
//   next();
// });

/////////////////////////////////////////////////////////////////////////
// tourSchema.index({ price: 1 });
tourSchema.index({ price: 1, ratingsAverage: -1 });
tourSchema.index({ slug: 1 });
tourSchema.index({ startLocation: '2dsphere' });
/////////////////////////////////////////////////////////////////////////
tourSchema.virtual('durationWeeks').get(function() {
  return this.duration / 7;
});
/////////////////////////////////////////////////////////////////////////
// Virtual populate
tourSchema.virtual('reviews', {
  ref: 'Review',
  foreignField: 'tour',
  localField: '_id'
});

/////////////////////////////////////////////////////////////////////////
// DOCUMENT MIDDLEWARE: runs before .save() and .create()
tourSchema.pre('save', function(next) {
  this.slug = slugify(this.name, { lower: true });
  next();
});

/////////////////////////////////////////////////////////////////////////
// QUERY MIDDLEWARE
// tourSchema.pre('find', function(next) {
tourSchema.pre(/^find/, function(next) {
  this.find({ secretTour: { $ne: true } });

  this.start = Date.now();
  next();
});

/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

tourSchema.pre(/^find/, function(next){
  this.populate({
    path: 'guides',
    select: '-__v -passwordChangedAt'
  });///populate can accept filtering or excluding fileds to refer
    
    next();
  });


/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////
  tourSchema.post(/^find/, function(docs, next) {
    console.log(`Query took ${Date.now() - this.start} milliseconds!`);
    next();
  });

/////////////////////////////////////////////////////////////////////////

// // AGGREGATION MIDDLEWARE

// tourSchema.pre('aggregate', function(next) {
//   this.pipeline().unshift({ $match: { secretTour: { $ne: true } } });

//   console.log(this.pipeline());
//   next();
// });

/////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////
const TourModel = mongoose.model('Tour', tourSchema);
module.exports = TourModel;
/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////
