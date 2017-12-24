(function(){
  angular.module('asm3biop')
  .factory('Settings', ['$resource', SettingsFactory]);

  function SettingsFactory($resource) {
    return $resource('/api/settings/:id');
  }
})();
