from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('interests/', views.interests_list, name='interests_list'),
    path('interests/<int:interests_id>/',
         views.posts_by_interests, name='posts_by_interests'),
    ]