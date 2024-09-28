# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,UserFeedView
from .views import LikePost, UnlikePost

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('<int:pk>/like/', LikePost.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePost.as_view(), name='unlike_post'),

]
