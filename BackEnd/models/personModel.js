const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const PersonSchema = new Schema({
  name: {
    type: String,
    required: [true, 'Please let us know you'],
    unique: true,
    lowercase: true,
  },
  account: {
    type: String,
    required: [true, 'Please let us know you'],
    lowercase: true,
  },
  embedding:{
    type: Array,
    required: [true, 'embedded data is required for a person to registry'],
  },
});

const PersonModel = mongoose.model('person_', PersonSchema);

module.exports = PersonModel;