(function(){
    angular.module('asm3biop')
    .factory('SocketFactory', ['socketFactory', SocketFactory]);
  
    function SocketFactory(socketFactory) {
      return socketFactory({
          ioSocket: io.connect("http://localhost:8080")
      });
    }
  })();
  