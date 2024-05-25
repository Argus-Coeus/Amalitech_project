from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('api/v1/',include('api.urls')),
    path('api-auth/',include('api.urls')),
    path('auth/', include('auths.urls')),
]
