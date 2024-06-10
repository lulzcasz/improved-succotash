from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from bleach import clean

from apps.posts.models import Post

@receiver(pre_save, sender = Post)
def generate_post_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save, sender = Post)
def clean_html(sender, instance, **kwargs):
    instance.body = clean(instance.body)
