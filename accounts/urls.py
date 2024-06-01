from django.urls import path
from  .views import LoginView,SignView



urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup/', SignView.as_view(), name = 'register'),
]