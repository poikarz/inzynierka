(function(){
  angular.module('asm3biop')
  .controller('NewSimulationController', ['$scope', 'DefaultSettings', 'Settings', NewSimulationController])

  function NewSimulationController($scope, DefaultSettings, Settings) {

    $scope.selectedSettingsName = null;
    // $scope.paramsName = ["fSI", "YSTOO2", "YSTONOX", "YHO2", "YHNOX", "YA", "fXI", "iNSI", "iNSS", "iNXI", "iNXS", "iNBM", "iSSXI", "iSSXS", "iSSBM", "SO2", "SI", "SS", "SNH4", "SN2", "SNOX", "SALK", "XI", "XS", "XH", "XSTO", "XA", "XSS", "kH", "kH10", "kH20", "KX", "kSTO", "niNOX", "KO2", "KNOX", "KS", "KSTO", "mikroH", "KNH4", "KALK", "bHO2", "bHNOX", "bSTOO2", "bSTONOX", "mikroA", "KANH4", "KAO2", "KAALK", "bAO2", "bANOX"];

    DefaultSettings.get(function(res) {
      $scope.defaultValues = res;
      $scope.paramsName = Object.keys(res);
      for(var i = 0; i < $scope.paramsName.length; i++) {
        if ($scope.paramsName[i].indexOf('$')>=0) {
          $scope.paramsName.splice(i, 1);
          i--;
        }
      }
    });

    Settings.query(function(res) {
      $scope.definedSettings = res;
    });

    $scope.selectSettings = function() {
      if ($scope.selectedSettingsName>=0) {
        $scope.settings = $scope.definedSettings[$scope.selectedSettingsName].values;
      } else {
        $scope.settings = null;
      }
    }

  }
})();
