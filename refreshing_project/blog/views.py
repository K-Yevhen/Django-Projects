# blog/views.py
from django.shortcuts import render
from .models import BlogPost
from weather_app.views import get_weather

def home(request):
    city = 'Krakow'  # Set a default city or get it dynamically based on user preferences
    api_key = 'bf450c16cbdb6dc861e255d179f8173f'  # Replace with your actual OpenWeatherMap API key
    weather_data = get_weather(city, api_key)

    print("Weather Data:", weather_data)  # Debug print

    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
        'city': city,
        'temperature': weather_data.get('main', {}).get('temp', 'N/A'),
        'description': weather_data.get('weather', [{}])[0].get('description', 'N/A'),
    }

    return render(request, 'blog/home.html', context)

