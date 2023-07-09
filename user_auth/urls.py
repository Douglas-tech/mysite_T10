from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('authenticate_user/user/<str:username>/', views.show_user, name='show_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
