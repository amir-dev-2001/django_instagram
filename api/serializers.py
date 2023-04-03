from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model
from content.models import Post, PostMedia
from location.models import Location
from activity.models import Comment

from relation.models import Relation

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'avatar', 'bio', 'is_verified')

class UserLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'bio', 'is_verified')


class RelationSerializer(serializers.ModelSerializer):
    from_user = UserLightSerializer()
    followed_back = serializers.SerializerMethodField()

    class Meta:
        model = Relation
        fields = ('from_user', 'followed_back', 'create_time')


    def get_followed_back(self, obj):
        return Relation.objects.filter(from_user=obj.to_user, to_user=obj.from_user).exists()        


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('title', 'points')

class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia        
        fields = ('media_type', 'media_file')

class PostListSerializer(serializers.ModelSerializer):
    user = UserLightSerializer()
    locations = LocationSerializer()
    media = PostMediaSerializer(many=True)
# TODO: add post_tag and tagged_users
# TODO: add likes and comments counts    
    class Meta:
        model = Post
        fields = ('id', 'user', 'caption', 'locations', 'media')
            

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment   
        fields = ('id', 'caption', 'post', 'reply_to')    


    # the method below only validates the caption. in this case does nothing
    # def validate_someFieldName => validates that field
    def validate_caption(self,attr):
        return attr     

    def validate(self, attrs):
        request = self.context['request']
        print(attrs['post'].user.is_private)

        if attrs['reply_to'] is not None:
            if attrs['reply_to'].post != attrs['post']:
                raise ValidationError(_("comment is not for the same post"))  
            
        if attrs['post'].user.is_private == True:    
            if request.user != attrs['post'].user and not Relation.objects.filter(
                from_user=request.user, to_user=attrs['post'].user).exists():
                raise ValidationError(_('You can not comment on this post. This account is private and you are not following it yet.'))
        return attrs    

class UsersAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

