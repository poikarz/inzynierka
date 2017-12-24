(function(){
  angular.module('asm3biop')
  .factory('DefaultSettings', ['$resource', DefaultSettingsFactory]);

  function DefaultSettingsFactory($resource) {
    return $resource('/api/defaultSettings');
  }
})();
