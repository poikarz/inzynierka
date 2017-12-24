(function () {
  angular.module('asm3biop')
    .factory('SocketFactory', ['socketFactory', '$location', SocketFactory]);

  function SocketFactory(socketFactory, $location) {
    return socketFactory({
      ioSocket: io.connect("http://" + $location.host() + ":" + $location.port())
    });
  }
})();
