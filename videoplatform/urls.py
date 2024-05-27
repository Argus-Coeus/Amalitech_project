from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('api/v1/',include('api.urls')),
    path('api-auth/',include('api.urls')),
    path('auth/', include('auths.urls')),
    path('account/', include('accounts.urls')),
    path('api/docs/', include_docs_urls(title='Video API'))
]
