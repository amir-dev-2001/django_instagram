from django.contrib import admin
from .models import Post, PostMedia, Tag, PostTag, TaggedUser

admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(TaggedUser)