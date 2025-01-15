from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField
from categories.models import Interests


class Course(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interests = models.ForeignKey(Interests, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    image = CloudinaryField('image', blank=True)
    description = models.TextField(default='Describe Event')
    location = models.CharField(max_length=255)
    spaces = models.IntegerField()
    interests = models.ForeignKey(Interests, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Community(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = SummernoteTextField(blank=True)
    members = models.ManyToManyField(User, related_name='communities', blank=True)
    interests = models.ManyToManyField(Interests, related_name='communities', blank=True)  # Use Interests directly
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    interests = models.ForeignKey(Interests, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f"Rating for {self.event.title} by {self.user.username}"