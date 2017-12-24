var settingsModel = require('../models/settings.js');

var exports = module.exports = {};

exports.readById = function(id) {
  return new Promise(function(resolve, reject) {
    settingsModel.find({_id: id}, function(error, data){
      if (error){
        console.log(error);
        reject();
      }
      resolve(buildResults(data)[0]);
    });
  });
}

exports.readDefaultSettings = function() {
  return new Promise(function(resolve, reject) {
    settingsModel.find({default: "true"}, function(error, data){
      if (error){
        console.log(error);
        reject();
      }
      resolve(data[0]['values']);
    });
  });
}

exports.readAll = function() {
  return new Promise(function(resolve, reject) {
    settingsModel.find({default: {$ne: true}}, function(error, data){
      if (error){
        console.log(error);
        reject();
      }
      resolve(buildResults(data));
    });
  });
}

exports.create = function(data) {
  return new Promise(function(resolve, reject) {
    settingsModel.create(data, function(error, data){
      if (error){
        console.log(error);
        reject();
      }
      debugger;
      resolve(buildResults(data)[0]);
    });
  });
}

function buildResults(data) {
  var res = [].concat(data);
  for (var i = 0; i < res.length; i++){
    var obj = res[i].toObject();
    obj.id = obj.id?obj.id:obj._id;
    delete obj._id;
    delete obj.__v;
    res[i] = obj;
  }
  return res;
}
