(function(){
  angular.module('asm3biop')
  .config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "templates/main.tmpl.html"
    })
    .when("/new", {
        templateUrl : "templates/new.tmpl.html",
        controller: 'NewSimulationController'
    })
    .when("/current", {
        templateUrl : "templates/current.tmpl.html",
        controller: 'CurrentSimulationController'
    })
    .when("/history", {
        templateUrl : "templates/history.tmpl.html"
    });
});
})();
