(function () {
  angular.module('asm3biop')
    .controller('CurrentSimulationController', ['$scope', '$compile', '$document', 'Execute', 'SocketFactory', 'ChartFactory', CurrentSimulationController])

  function CurrentSimulationController($scope, $compile, $document, Execute, SocketFactory, ChartFactory) {
    
    $scope.options = ChartFactory.options;
    
    $scope.data = ChartFactory.data;
    
    SocketFactory.on('asmScript', function (data) {
      ChartFactory.prepareData(data);
    })

    Execute.execute('5');
  }
})();
