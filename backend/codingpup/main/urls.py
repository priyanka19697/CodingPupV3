"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from profiles.views  import ChangePasswordView, LogoutView, HomeView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .openapi_info import openapi_info
from rest_framework_simplejwt import views as jwt_views

schema_view = get_schema_view(
    openapi_info,
    public=True
)

urlpatterns = [
    path('home/', HomeView.as_view(), name ='home'),

    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('profiles/', include('profiles.urls')),
        path('blogs/', include('blog.urls')),
        path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    ])),
    path('api-auth/', include('rest_framework.urls')),

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
