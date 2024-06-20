from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('api.urls')),
    path('auth/', include('auths.urls')),
    path('', include('accounts.urls')),
    path('api/docs/', include_docs_urls(title='Video API'),name= "docs"),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
