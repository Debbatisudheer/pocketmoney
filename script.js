document.addEventListener('DOMContentLoaded', function () {
    // Get the canvas element
    var ctx = document.getElementById('animatedChart').getContext('2d');

    // Create the doughnut chart
    var doughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Shopping', 'Movies', 'Food', 'Technology', 'Charitable Contributions', 'Miscellaneous'],
            datasets: [{
                data: [11, 5, 10, 45, 10, 19],
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4CAF50', '#FF5733', '#8B4513'],
            }]
        },
        options: {
            animation: {
                animateRotate: true,
                animateScale: true
            },
            plugins: {
                annotation: {
                    annotations: [
                        {
                            type: 'text',
                            mode: 'point',
                            x: '100%', // Horizontal center
                            y: '90%', // Adjust the vertical position
                            fontSize: 26,
                            fontColor: '#000', // Black color
                            text: '@sudheer debbati', // Your name
                            textAlign: 'center',
                            enabled: true,
                            rotation: 200, // Horizontal rotation
                        }
                    ]
                }
            }
        }
    });
});