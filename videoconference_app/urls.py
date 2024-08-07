from django.urls import path
from . import views

urlpatterns = [
    path('meeting/', views.videocall, name='meeting'),
    path('', views.index, name='index'),
]
