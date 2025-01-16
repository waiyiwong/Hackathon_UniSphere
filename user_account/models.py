from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField
from categories.models import Interests
from events.models import Course, Event, Community, Rating, Ticket

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = SummernoteTextField(blank=True)
    profile_picture = CloudinaryField('image', blank=True)
    interests = models.ManyToManyField(Interests, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
    communities = models.ManyToManyField(Community, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    tickets = models.ManyToManyField(Ticket, blank=True)
    ratings = models.ManyToManyField(Rating, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
