from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, Event, Community, Rating, Ticket

# Register your models here.
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'event_date', 'location', 'spaces', 'interests', 'course', 'status', 'approved', 'created_on')
    search_fields = ['title', 'user__username']
    list_filter = ('status', 'approved')
    summernote_fields = ('description',)


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'user', 'interests', 'approved', 'created_on')
    search_fields = ['name', 'user__username']
    list_filter = ('approved',)
    summernote_fields = ('description',)


@admin.register(Community)
class CommunityAdmin(SummernoteModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'approved')
    search_fields = ['name']
    list_filter = ('approved',)
    summernote_fields = ('description',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'event', 'interests', 'approved', 'created_on')
    search_fields = ['user__username', 'event__title']
    list_filter = ('rating', 'approved')
    summernote_fields = ('comment',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_holder', 'date_issued', 'event', 'approved', 'created_on')
    search_fields = ['ticket_holder__username', 'event__title']
    list_filter = ('approved',)