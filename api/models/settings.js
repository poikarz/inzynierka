var mongoose = require('mongoose');

var settingsSchema = mongoose.Schema({
	name : String,
	default : Boolean,
	values : Object
});

module.exports = mongoose.model('settings', settingsSchema);
