from django.urls import path
from .views import SignView,ForgotPassword,ForgotPasswordConfirm,Upload,user_list,video_detail,logout,Homepage,admin_list
from .views import LoginView
urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup/', SignView.as_view(), name = 'register'),
    path('forgot-password/', ForgotPassword.as_view(), name = 'forgot-password'),
    path('reset-password-confirm/', ForgotPasswordConfirm.as_view(), name = 'reset-password-confirm'),
    path('upload/', Upload.as_view(), name = 'upload'),
    path('dashboard/', user_list, name='video_list'),
    path('super/', admin_list, name='admin_list'),
    path('video/<int:video_id>/', video_detail, name='video_detail'),
    path('logout/', logout , name='logout'),
    path('', Homepage.as_view() , name='homepage'),
]