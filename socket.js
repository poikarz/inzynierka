
var io;
module.exports = {
    connect: function (http) {
        io = require('socket.io')(http);
        io.sockets.on('connection', function (socket) {
            console.log('connected')
        })
    },
    emit: function (data) {
        io.sockets.emit('asmScript', data)
    }
}