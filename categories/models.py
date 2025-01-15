from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Interests(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interests")

    def __str__(self):
        return self.name