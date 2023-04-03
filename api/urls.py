from django.urls import path
from .views import ProfileRetrieveUpdateApiView, ProfileRetrieveApiView, FollowersListApiView, PostListApiView, CommentCreateApiView, UsersListApiView, FollowingsListApiView

urlpatterns = [
    path('profile/', ProfileRetrieveUpdateApiView.as_view()),
    path('profile/<str:username>/', ProfileRetrieveApiView.as_view()),
    path('followers/', FollowersListApiView.as_view()),
    path('contents/<str:username>', PostListApiView.as_view()),
    path('activity/comment', CommentCreateApiView.as_view()),
    path('activity/like', CommentCreateApiView.as_view()),
    path('followings/', FollowingsListApiView.as_view()),
    
    # admin api
    path('admin/users/', UsersListApiView.as_view()),
    # path('admin/', ProfileRetrieveUpdateApiView.as_view()),
    # path('admin/', ProfileRetrieveUpdateApiView.as_view()),

]
