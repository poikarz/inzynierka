(function () {
  angular.module('asm3biop')
    .factory('ChartFactory', [ChartFactory]);

  function ChartFactory() {

    var data = [
      {
        values: [],
        key: 'SO2dp',
        color: '#5f707e'
      },
      {
        values: [],
        key: 'SIdp',
        color: '#ff7f0e'
      },
      {
        values: [],
        key: 'SSdp',
        color: '#ff70fe'
      },
      {
        values: [],
        key: 'SNH4dp',
        color: '#ff7ff4'
      },
      {
        values: [],
        key: 'SN2dp',
        color: '#3f7f0e'
      },
      {
        values: [],
        key: 'SNOXdp',
        color: '#f01f0e'
      },
      {
        values: [],
        key: 'SALKdp',
        color: '#f55f0e'
      },
      {
        values: [],
        key: 'XIdp',
        color: '#7f7f5e'
      },
      {
        values: [],
        key: 'XSdp',
        color: '#057f14'
      },
      {
        values: [],
        key: 'XSTOdp',
        color: '#ff000e'
      },
      {
        values: [],
        key: 'XAdp',
        color: '#ff450e'
      },
      {
        values: [],
        key: 'XSSdp',
        color: '#45450e'
      },
    ];

    var options = {
      chart: {
        type: 'lineChart',
        height: 450,
        x: function (d) {
          console.log(d)
          return d.x; 
        },
        y: function (d) {
          return d.y; 
        },
        useInteractiveGuideline: true,
        xAxis: {
          axisLabel: 'Time'
        },
        yAxis: {
          axisLabel: 'SO2dp',
          tickFormat: function (d) {
            return d3.format('.02f')(d);
          },
          axisLabelDistance: -10
        },
      },
    };

    function prepareData(res) {
      console.log(res)
      this.data[0].values.push({
        x: res.time,
        y: res.phase1.SO2dp
      });
      
      this.data[1].values.push({
        x: res.time,
        y: res.phase1.SIdp
      });
      
      this.data[2].values.push({
        x: res.time,
        y: res.phase1.SSdp
      });
      
      this.data[3].values.push({
        x: res.time,
        y: res.phase1.SNH4dp
      });
      
      this.data[4].values.push({
        x: res.time,
        y: res.phase1.SN2dp
      });
      
      this.data[5].values.push({
        x: res.time,
        y: res.phase1.SNOXdp
      });
      
      this.data[6].values.push({
        x: res.time,
        y: res.phase1.SALKdp
      });
      
      this.data[7].values.push({
        x: res.time,
        y: res.phase1.XIdp
      });
      
      this.data[8].values.push({
        x: res.time,
        y: res.phase1.XSdp
      });
      
      this.data[9].values.push({
        x: res.time,
        y: res.phase1.XSTOdp
      });
      
      this.data[10].values.push({
        x: res.time,
        y: res.phase1.XAdp
      });
      
      this.data[11].values.push({
        x: res.time,
        y: res.phase1.XSSdp
      });
    }
    return {
      data: data,
      options: options,
      prepareData: prepareData
    };
  }
})();
