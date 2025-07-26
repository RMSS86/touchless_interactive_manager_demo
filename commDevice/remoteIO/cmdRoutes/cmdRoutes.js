const express = require("express");
const router = express.Router();

router.route("/:cmd").get(ioController).post(ioController.sendCMD);

module.exports = router;
