from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ['user__username']
    summernote_fields = ('profile_picture',)