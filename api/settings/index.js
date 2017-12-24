var settings = require('./settings.js');

module.exports = {
  readById: settings.readById,
  readDefaultSettings: settings.readDefaultSettings,
  readAll: settings.readAll,
  create: settings.create
}
