const catchAsync = require('../utils/catchAsync');
const AppError = require('../utils/appError');
const APIFeatures = require('../utils/apiFeatures');
const factory = require('./handlerFactory')
const _Person =require('../models/personModel');

exports.getAllPeople = factory.getAll(_Person);
exports.createPerson = factory.createOne(_Person);
exports.deletePerson = factory.deleteOne(_Person);
exports.getPerson = factory.getOne(_Person);
