from django.db.models import (
    Model, TextChoices,
    CharField, TextField, DateTimeField, SlugField
)

class PostCategory(TextChoices):
    PROJECT = 'project', 'Project'
    ARTICLE = 'article', 'Article'

class Post(Model):
    title = CharField(max_length = 128, unique = True)
    slug = SlugField(max_length = 128, unique = True, blank = True)
    body = TextField()
    category = CharField(max_length = 7, choices = PostCategory.choices)
    created_at = DateTimeField(auto_now_add = True)
    updated_at = DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
