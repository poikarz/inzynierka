var mongoose = require('mongoose');
var express = require('express');
var mongoose = require('mongoose');
var morgan = require('morgan');
var bodyParser = require('body-parser');
var methodOverride = require('method-override');
var socket = require('./socket.js')

var port = process.env.PORT || 8080;
var app = express();


mongoose.connect('mongodb://localhost:27017/ASM3bioP');

app.use(express.static(__dirname + '/web'));
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({'extended':'true'}));
app.use(bodyParser.json());
app.use(bodyParser.json({ type: 'application/vnd.api+json' }));
app.use(methodOverride());

require('./api/routes/routes.js')(app);
require('./api/routes/settings.js')(app);
require('./api/routes/execute.js')(app);

var http = require('http').Server(app);

socket.connect(http)

http.listen(port);
console.log("App listening on port " + port);
