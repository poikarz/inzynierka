(function(){
  angular.module('asm3biop', ['btford.socket-io', 'nvd3', 'ngMaterial', 'ngRoute', 'ngResource'])
  
  .config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('blue-grey')
      .accentPalette('deep-orange')
      .warnPalette('red')
      .backgroundPalette('grey');
  });
})();
