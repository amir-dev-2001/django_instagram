from django.urls import path
from .views import ProfileRetrieveUpdateApiView, ProfileRetrieveApiView, FollowersListApiView, PostListApiView, CommentCreateApiView

urlpatterns = [
    path('profile/', ProfileRetrieveUpdateApiView.as_view()),
    path('profile/<str:username>/', ProfileRetrieveApiView.as_view()),
    path('followers/', FollowersListApiView.as_view()),
    path('contents/<str:username>', PostListApiView.as_view()),
    path('activity/comment', CommentCreateApiView.as_view()),
]
