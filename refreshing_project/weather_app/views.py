# weather_app/views.py
import requests
from django.shortcuts import render


def get_weather(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # You can change this to 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data


def weather(request):
    city = request.GET.get('city', 'Krakow')  # Default to London if city not provided
    api_key = 'bf450c16cbdb6dc861e255d179f8173f'  # Replace with your actual API key
    weather_data = get_weather(city, api_key)

    context = {
        'city': city,
        'temperature': weather_data.get('main', {}).get('temp', 'N/A'),
        'description': weather_data.get('weather', [{}])[0].get('description', 'N/A'),
    }

    return render(request, 'weather_app/weather.html', context)
