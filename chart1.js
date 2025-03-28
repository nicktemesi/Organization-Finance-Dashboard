document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById('line_chart');

  new Chart(ctx, {
  type: 'line',
  data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June','Jul', 'Aug', 'Sept', 'Oct', 'Nov','Dec'],
      datasets: [{
        label: 'Expenses vs Revenue',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
  },
  options: {
      scales: {
      y: {
          beginAtZero: true
      }
      }
  }
  });
});