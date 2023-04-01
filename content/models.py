from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import BaseModel
from django.contrib.auth import get_user_model 
from location.models import Location
from django.core.validators import FileExtensionValidator

User = get_user_model()

class Post(models.Model):
    caption = models.TextField(_('caption'), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='posts', null=True,blank=True)
    create_time = models.DateTimeField(_("created time") ,auto_now_add=True)
    modified_time = models.DateTimeField(_("modified time") ,auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.user.username, self.id)
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

class PostMedia(models.Model):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHOICES = (
        (IMAGE, _('Image')),
        (VIDEO, _('Video')),
    )

    media_type = models.PositiveSmallIntegerField(_('media type'), choices=TYPE_CHOICES, default=IMAGE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media_file = models.FileField(
        _('media file'), upload_to='content/media', 
        validators=[FileExtensionValidator(allowed_extensions=('mp4', 'png', 'jpg', 'jpeg', 'flv'))]
    )
    create_time = models.DateTimeField(_("created time") ,auto_now_add=True)
    modified_time = models.DateTimeField(_("modified time") ,auto_now=True)

    def __str__(self):
        return "{} - {}".format(str(self.post), self.get_media_type_display())

    class Meta:
        verbose_name = _('post media')
        verbose_name_plural = _('post medias')

class Tag(models.Model):
    title = models.CharField(_('title'), max_length=255)
    create_time = models.DateTimeField(_("created time") ,auto_now_add=True)
    modified_time = models.DateTimeField(_("modified time") ,auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags') 

class PostTag(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='hashtags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return "{} - {}".format(str(self.tag), str(self.post))

    class Meta:
        verbose_name = _('post tag')
        verbose_name_plural = _('post tags')

class TaggedUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tagged_users')
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tagged_posts')

    def __str__(self):
        return "{} - {}".format(str(self.user), str(self.Post))
    
    class Meta:
        verbose_name = _('tagged user')
        verbose_name_plural = _('tagged users')