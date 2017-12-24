var execute = require('../execute/index.js')

module.exports = function(app) {
  app.post('/api/execute/:id', function(req, res) {
    execute.run().then(function(data){
      res.json(data);
    });
  });
};
