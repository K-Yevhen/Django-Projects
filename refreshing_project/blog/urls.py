from django.urls import path, include
from .views import home, like_post, add_comment, register
from .api_views import BlogPostListAPIView, BlogPostDetailAPIView, LikeListCreateAPIView, CommentListCreateAPIView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
    path('api/posts/', BlogPostListAPIView.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', BlogPostDetailAPIView.as_view(), name='api_post_detail'),  # Use 'pk' as the parameter
    path('api/likes/', LikeListCreateAPIView.as_view(), name='api_like_list_create'),
    path('api/comments/', CommentListCreateAPIView.as_view(), name='api_comment_list_create'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
