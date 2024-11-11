from django.contrib import admin
from django.urls import path, include
from .views import get_users, create_user, User_detail  

urlpatterns = [    
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>/', User_detail, name='user_detail'),  # Add your API URLs here
]