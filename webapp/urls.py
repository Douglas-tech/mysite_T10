from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('portfolio/', views.portfolio),
]