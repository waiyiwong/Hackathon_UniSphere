from django import forms
from .models import Course, Event, Community, Ticket, Interests, Rating


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

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'interests': forms.Select(choices=Interests.objects.all().values_list('id', 'name')),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }