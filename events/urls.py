from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('events/', views.event_list, name='event_list'),
    path('communities/', views.community_list, name='community_list'),
    path('eventsandcourses/', views.events_and_courses, name='eventsandcourses'),
]