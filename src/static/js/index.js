
// Global variables
let myChart = null;

$(document).ready(function(){
    $("#hashtag").keydown( 
        function(e){
        if (e.keyCode == 13) { 
            e.preventDefault();

            var hashtag = document.getElementById("hashtag").value;
            console.log("Hashtag: " + hashtag);

            hashtag = hashtag.replace('#', '');
            console.log("Hashtag 2: " + hashtag)

            fetch('http://127.0.0.1:5000/hashtag?hashtag=' + hashtag,
                {
                    method: 'GET',
                    body: null
                })
                .then(res => res.json())
                .then(res => {

                        emotions = res['emotion']['document']['emotion'];
                        console.log(emotions);

                        var sadness = emotions['sadness']*100;
                        var joy = emotions['joy']*100;
                        var fear = emotions['fear']*100;
                        var disgust = emotions['disgust']*100;
                        var anger = emotions['anger']*100;
            
                        var yValues = [sadness, joy, fear, disgust, anger];
        
                        makeChart(yValues, hashtag);
                });
        }
    });
});

function makeChart(yValues, hashtag) {
    var xValues = ['Sadness', 'Joy', 'Fear', 'Disgust', 'Anger'];

    let ctx = document.getElementById("emotionsChart").getContext('2d');

    if (myChart != null) {
        console.log('Destroy Chart!')
        myChart.destroy();
    }

    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: xValues,
          datasets: [{
            data: yValues,
            borderColor: 'rgb(54, 162, 235)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderWidth: 1,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            plugins: {
                legend: {display: false},
                title: {
                    display: true,
                    text: "Public Emotion on " + hashtag
                },
            },
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
      });
};