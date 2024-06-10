from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name = 'schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name = 'schema'), name = 'redoc'),
]

urlpatterns += [
    path('api/', include('apps.posts.urls')),
]
