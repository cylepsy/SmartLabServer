google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawtemp);
google.charts.setOnLoadCallback(drawhum);
google.charts.setOnLoadCallback(drawlight);
function drawtemp() {


      var query = new google.visualization.Query(
          'https://docs.google.com/spreadsheets/d/13MfNqhYh4rTB7Q54R3Ol-TooSU5_6JqACszmosTTB4U/edit?usp=sharing&sheet=Sheet4');
      query.send(handleQueryResponse);
    }

function handleQueryResponse(response) {
      if (response.isError()) {
        alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
      }
      var options = {
           title: 'Temperature of my room',
           height: 400,
         };


      var data = response.getDataTable();
      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

      chart.draw(data, options);
    }

    function drawhum() {


          var query = new google.visualization.Query(
              'https://docs.google.com/spreadsheets/d/13MfNqhYh4rTB7Q54R3Ol-TooSU5_6JqACszmosTTB4U/edit?usp=sharing&sheet=Sheet2');
          query.send(handleQueryResponse2);
        }

    function handleQueryResponse2(response) {
          if (response.isError()) {
            alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
            return;
          }
          var options = {
               title: 'Humidity of my room',
               height: 400,
             };


          var data = response.getDataTable();
          var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));

          chart.draw(data, options);
        }
        function drawlight() {


              var query = new google.visualization.Query(
                  'https://docs.google.com/spreadsheets/d/13MfNqhYh4rTB7Q54R3Ol-TooSU5_6JqACszmosTTB4U/edit?usp=sharing&sheet=Sheet3');
              query.send(handleQueryResponse3);
            }

        function handleQueryResponse3(response) {
              if (response.isError()) {
                alert('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
                return;
              }
              var options = {
                   title: 'Lightlevel of my room',
                   height: 400,
                 };


              var data = response.getDataTable();
              var chart = new google.visualization.LineChart(document.getElementById('chart_div3'));

              chart.draw(data, options);
            }
