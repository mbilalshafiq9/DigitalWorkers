// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Photographer", "Event Planner", "Car Washer", "Pickup/Delivery"],
    datasets: [{
      data: [12, 15, 11, 8],
      backgroundColor: ['#FC8370', '#FECB3E', '#C2549D', '#7E549E'],
    }],
  },
});
