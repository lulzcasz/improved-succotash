from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
