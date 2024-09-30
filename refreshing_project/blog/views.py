# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment, Like
from django.contrib import messages
from weather_app.views import get_weather
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


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

    return render(request, 'blog/base.html', context)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    user = request.user

    # Check if the user has already liked the post
    if post.likes.filter(user=user).exists():
        post.likes.filter(user=user).delete()
        liked = False
    else:
        Like.objects.create(user=user, blog_post=post)
        liked = True

    data = {
        'liked': liked,
        'likes_count': post.likes.count(),
    }

    return JsonResponse(data)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    user = request.user
    comment_text = request.POST.get('comment_text')

    if comment_text:
        Comment.objects.create(user=user, blog_post=post, comment_text=comment_text)

    # Redirect to the 'home' view (or another appropriate view)
    return redirect('blog:home')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')  # Redirect to home or any other page
    else:
        form = UserRegistrationForm()

    return render(request, 'blog/registration/register.html', {'form': form})
