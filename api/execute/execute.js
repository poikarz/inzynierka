var PythonShell = require('python-shell');
var moment = require('moment');
var socket = require('../../socket.js');

var exports = module.exports = {};

var pythonShellOptions = {
  pythonPath: '/usr/bin/python3.5',
  executable: 'python3',
};

exports.run = function (id) {
  return new Promise(function (resolve, reject) {
    var asmScript = new PythonShell('api/asm3/asm.py', pythonShellOptions),
      result = [],
      i = 0;

    asmScript.on('message', function (message) {
      var parsedMessage = JSON.parse(message);
      if (i++ % 1000 == 0) {
        socket.emit(parsedMessage);
      }
      result.push(parsedMessage)
    });

    asmScript.end(function (err) {
      if (err) {
        reject(err);
      }
      resolve(result);
    });
  });
}
