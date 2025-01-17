from django import forms
from .models import Profile
from django_summernote.widgets import SummernoteWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'bio': SummernoteWidget(),
        }
        fields = ['profile_picture', 'bio', 'interests', 'events', 'tickets', 
                  'courses', 'communities', 'ratings']
