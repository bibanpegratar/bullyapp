from django.urls import path
from .views import *

#create url for user validation
urlpatterns = [
    path('users/', UserAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('posts/', PostsAPIView.as_view(), name='posts'),
    path('posts/<int:fk>/', UserPostsAPIView.as_view(), name='user_posts'),
    path('posts/<int:fk>/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('comments/', CommentsAPIView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail')
]