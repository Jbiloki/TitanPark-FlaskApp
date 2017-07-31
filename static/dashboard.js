function loadFakeData(){
  function getRandomInteger(min, max){
     return Math.floor(Math.random() * (max - min)) + min;
  }

  function generateFakeTimeseries(min, max){
    var data = [];
    for(var i = 0; i < 24; i++){
      data.push([moment().subtract(i, 'hour').valueOf(), getRandomInteger(min, max)])
    }
    return data;
  }

  var data = {};
      data.parking_status = {
        eastside: generateFakeTimeseries(0, 100),
        nutwood: generateFakeTimeseries(0, 2000),
        state_college: generateFakeTimeseries(200, 1500),
        lot_a_and_g: generateFakeTimeseries(300, 400),
      }
      data.parking_capacities = {
        eastside: 100,
        nutwood: 2000,
        state_college: 1500,
        lot_a_and_g: 400,
      }

  return data;
}



function loadData(){
  data = loadFakeData();

  setParkingCharts(data);
  setParkingHealth(data);
}


$(document).ready(function(){
  // website started

  $(".content .grid").gridster({
       widget_margins: [20, 20],
       widget_selector: '.chart',
       widget_base_dimensions: [200, 200]
   });

   loadData();

})

function setParkingHealth(data){
  function determineStatus(value, max){
    if(value/max === 1){
      return '<span class="status-full">Full</span>';
    }

    if(value/max >= 0.9 ){
      return '<span class="status-poor">Poor</span>';
    }

    if(value/max >= 0.5){
      return '<span class="status-fair">Fair</span>';
    }

      return '<span class="status-healthy">Healthy</span>';
  }

  $("#parking-health").html('<div class="parking-health-bar bold">Parking Lot Health</div>')
  for(var i in data.parking_status){
    var parkingCount = data.parking_status[i];
    var html = ''
        html += '<div class="parking-health-bar">';
        html += '<div class="parking-health-name">' + i.replace(/_/g, ' ') + '</div>';
        html += '<div class="parking-health-status">' + determineStatus(parkingCount[parkingCount.length - 1][1], data.parking_capacities[i]) + '</div>';

    $("#parking-health").append(html)
  }
}

function setParkingCharts(data){
  const defaultxAxis = {
      type: 'datetime',
      tickInterval: 3600 * 1000,
      min: moment().subtract(1, 'days'),
      max: moment().subtract(0, 'days'),
  };

  for(var i in data.parking_status){
    $('#parking-' + i).highcharts({
       chart: {
           zoomType: 'x'
       },
       title: {
        text: i.replace(/_/g, ' ')
      },
      yAxis: {
          title: {
              text: ''
          }
      },
      subtitle: {
        text: 'Parking Capacity'
      },
       xAxis: defaultxAxis,
       series: [{
           name: 'Lots Occupied',
           data: data.parking_status[i],
           pointStart: Date.UTC(2012, 05, 22),
           pointInterval: 24 * 3600 * 1000 // one day
       }]
    });
  }


}
