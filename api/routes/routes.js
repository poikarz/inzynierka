module.exports = function(app) {
	app.get('/', function(req, res) {
		res.sendfile('./web/index.html');
	});
};
