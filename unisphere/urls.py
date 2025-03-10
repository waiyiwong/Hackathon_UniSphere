"""
URL configuration for unisphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from categories.views import categories
from events.views import events_and_courses
from events.views import event_list
from user_account.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('categories.urls')),
    path('interests/', categories, name='interests'),
    path("about/", include("about.urls"), name="about-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('eventsandcourses/', events_and_courses, name='eventsandcourses'),
    path('', include('events.urls')),
    path("", include("home.urls"), name="home-urls"),
    path('profile/', profile, name='profile'),
    path('', include('user_account.urls')),
    path("accounts/", include("allauth.urls")),
]

