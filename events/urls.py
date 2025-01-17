from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('events/', views.event_list, name='event_list'),
    path('communities/', views.community_list, name='community_list'),
    path('eventsandcourses/', views.events_and_courses, name='eventsandcourses'),
    path('manage_items/', views.manage_items, name='manage_items'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('edit_community/<int:community_id>/', views.edit_community, name='edit_community'),
    path('delete_community/<int:community_id>/', views.delete_community, name='delete_community'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
]