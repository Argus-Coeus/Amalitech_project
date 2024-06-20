from django.urls import path
from .views import MyObtainTokenPairView,RegisterView,LogoutView, VerifyAccountView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('verify/<str:uid>/<str:token>/', VerifyAccountView.as_view(), name='verify-account'),
]
    
