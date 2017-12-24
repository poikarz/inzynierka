(function(){
  angular.module('asm3biop')
  .controller('ToolbarController', ['$scope', '$location', ToolbarController])

  function ToolbarController($scope, $location) {
    $scope.menuItems = [{
      name: "New simulation",
      path: "/new"
    }, {
      name: "Current simulations",
      path: "/current"
    }, {
      name: "History",
      path: "/history"
    }];

    $scope.goTo = function (path) {
      $location.path(path)
    }

  }
})();
