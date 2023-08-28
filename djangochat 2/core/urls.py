from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('messages/<str:username>/', views.private_messages, name='private_messages'),
    path('send_message/<str:username>/', views.send_private_message, name='send_private_message'),
    path('individual_chats/', views.individual_chats, name='individual_chats'),
]

