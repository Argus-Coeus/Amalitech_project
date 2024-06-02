from django.urls import path
from  .views import LoginView,SignView,ForgotPassword,ForgotPasswordConfirm



urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup/', SignView.as_view(), name = 'register'),
    path('forgot-password/', ForgotPassword.as_view(), name = 'forgot-password'),
    path('reset-password-confirm/', ForgotPasswordConfirm.as_view(), name = 'reset-password-confirm'),
]