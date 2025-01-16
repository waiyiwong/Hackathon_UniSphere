from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
    path('profile/', views.profile, name='profile'),
]