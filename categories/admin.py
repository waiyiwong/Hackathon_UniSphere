from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Interests

# Register your models here.
@admin.register(Interests)
class Interests(SummernoteModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'id')