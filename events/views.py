from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events_courses(request):
    return HttpResponse("Hello, Events and Courses!")
