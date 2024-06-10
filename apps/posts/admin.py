from django.contrib.admin import ModelAdmin, register

from apps.posts.models import Post

@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'category', )
    readonly_fields = ('slug', )
