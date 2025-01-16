from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('profile/', views.profile, name='profile'),
]