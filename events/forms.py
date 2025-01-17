from django import forms
from .models import Course, Event, Community, Ticket


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'