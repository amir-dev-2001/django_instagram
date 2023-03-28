from django.urls import path
from relation.views import FollowView

urlpatterns = [
    path('<str:username>', FollowView.as_view(), name='follow'),
]