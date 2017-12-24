(function(){
    angular.module('asm3biop')
    .factory('Execute', ['$http', ExecuteFactory]);
  
    function ExecuteFactory($http) {
      return {
        execute: execute,
      }

      function execute(settingsId){
        return $http({
          method: 'POST',
          url: 'api/execute/' + settingsId
        })
      }
    }
  })();
  