"""
URL configuration for whistle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:

    2. Add a URL to urlpatterns:  path('', views.home, name='home')

    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/',include('api.urls'))
] + debug_toolbar_urls()

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)