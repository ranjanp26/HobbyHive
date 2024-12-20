from django.urls import path
from .views import PostListCreateView, LikePostView, CommentCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='create-post'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/comment/', CommentCreateView.as_view(), name='create-comment'),
]
