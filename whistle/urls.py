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
from .views import api_root_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Whistle API",
      default_version='v1',
      description="Social Media Project Api using drf",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mohsinibnaftab@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('',api_root_view),
    path('api/v1/',include('api.urls'),name='api-root'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + debug_toolbar_urls()

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)