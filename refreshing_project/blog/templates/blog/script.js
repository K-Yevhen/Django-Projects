// script.js
function getWeather() {
    var cityInput = document.getElementById('cityInput');
    var cityNameSpan = document.getElementById('cityName');
    var temperatureSpan = document.getElementById('temperature');
    var descriptionSpan = document.getElementById('description');

    var city = cityInput.value.trim();

    if (city !== '') {
        fetch('/weather/?city=' + encodeURIComponent(city))
            .then(response => response.json())
            .then(data => {
                cityNameSpan.textContent = city;
                updateWeather(data);
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
            });
    }
}

function updateWeather(data) {
    var temperatureSpan = document.getElementById('temperature');
    var descriptionSpan = document.getElementById('description');

    var temperature = data.main && data.main.temp ? data.main.temp.toFixed(2) : 'N/A';
    var description = data.weather && data.weather[0] && data.weather[0].description ? data.weather[0].description : 'N/A';

    temperatureSpan.textContent = temperature;
    descriptionSpan.textContent = description;
}