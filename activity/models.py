from django.db import models
from django.utils.translation import ugettext_lazy as _
from lib.common_models import BaseModel
from django.contrib.auth import get_user_model 
from content.models import Post

User = get_user_model()

class Comment(BaseModel):
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    
class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return "{} >> {}".format(self.user.username, self.post.id)
    

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

                             



