from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Interests

# Register your models here.
@admin.register(Interests)
class Interests(SummernoteModelAdmin):
    list_display = ('name', 'formatted_description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    summernote_fields = ('description',)

    def formatted_description(self, obj):
        return format_html(obj.description)
    formatted_description.short_description = 'Description'
