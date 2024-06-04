from django.urls import path
from .views import MyObtainTokenPairView,RegisterView,LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomPasswordResetConfirmView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
]