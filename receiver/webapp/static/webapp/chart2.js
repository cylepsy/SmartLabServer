google.charts.load('current', {packages: ['corechart', 'line']});

google.setOnLoadCallback(drawVisualization);
function drawVisualization(){
  var jsonData = $.ajax({

        url: "static/webapp/data2.json",
        dataType:"json",
        async: false
        }).responseText;
  var data = google.visualization.DataTable(jsonData);
  var options = {
       title: 'Status of my room',
       height: 400,
     };
  var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}


