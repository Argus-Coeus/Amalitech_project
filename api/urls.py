from django.urls import path
from .views import PostList,PostDetail,UserDetail,UserList,api_root,CreateList

urlpatterns = [
    path('create/',CreateList.as_view(),name='create'),
    path('vd/',PostList.as_view(),name='listing'),
    path('',api_root),
    path('vd/<int:pk>/', PostDetail.as_view(),name='create-view'),
    path('users/', UserList.as_view(),name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(),name='users-listing'),
]
