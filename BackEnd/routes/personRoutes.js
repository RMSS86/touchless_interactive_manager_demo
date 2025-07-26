const fs = require('fs');
const path = require('path');
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const _PersonController = require('../controllers/personController')

const router = express.Router();

router
  .route('/')
  .get(_PersonController.getAllPeople)
  .post(_PersonController.createPerson);
   
router
    .route('/:id')
    .get(_PersonController.getPerson)
    .delete(_PersonController.deletePerson);

module.exports = router;