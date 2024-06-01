from django.urls import path
from  .views import LoginView,SignView,ForgotPassword



urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup/', SignView.as_view(), name = 'register'),
    path('forgot-password/', ForgotPassword.as_view(), name = 'forgot-password'),
]