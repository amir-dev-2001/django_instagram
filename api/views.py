from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication 
from .serializers import UserSerializer, RelationSerializer, PostListSerializer, CommentSerializer, UsersAdminSerializer
from rest_framework import generics
from relation.models import Relation
from content.models import Post

User = get_user_model()

class ProfileRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    
class ProfileRetrieveApiView(generics.RetrieveAPIView):    
    # first way of doing this 
    # using from rest_framework.views import APIView 
    '''
    def get(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND
            )    
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)
    '''
    # second way of doing this 
    # using from rest_framework.views import APIView 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'


class FollowersListApiView(generics.ListAPIView):
    queryset = Relation.objects.select_related('from_user').all()
    serializer_class = RelationSerializer
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(to_user=self.request.user)
    
class FollowingsListApiView(generics.ListAPIView):
    queryset = Relation.objects.select_related('from_user').all()
    serializer_class = RelationSerializer
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(to_user=self.request.user)


class PostListApiView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = 'username'
    lookup_field = 'user'


class CommentCreateApiView(generics.CreateAPIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UsersListApiView(generics.ListAPIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UsersAdminSerializer
