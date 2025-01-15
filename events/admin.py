from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course, Event, Community, Rating, Interests

# Register your models here.
@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'user', 'interests')
    summernote_fields = ('description',)


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'event_date', 'location', 'spaces', 'interests', 'course', 'status')
    summernote_fields = ('description',)


@admin.register(Community)
class CommunityAdmin(SummernoteModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    summernote_fields = ('description',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment', 'event', 'interests')