var settings = require('../settings/index.js')

module.exports = function(app) {
  app.get('/api/settings', function(req, res) {
    settings.readAll().then(function(data){
      res.json(data);
    });
  });

  app.post('/api/settings', function(req, res) {
    settings.create(req.body).then(function(data){
      res.json(data);
    });
  });

  app.get('/api/settings/:id', function(req, res) {
    settings.readById(req.params.id).then(function(data){
      res.json(data);
    });
  });

  app.get('/api/defaultSettings', function(req, res) {
    settings.readDefaultSettings().then(function(data){
      res.json(data);
    });
  });

  app.post('/api/settings/:id', function(req, res) {

  });

  app.delete('/api/settings/:id', function(req, res) {

  });
};
