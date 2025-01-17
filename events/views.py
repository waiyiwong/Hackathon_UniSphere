from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Event, Community, Rating, Ticket
from categories.models import Interests
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def events_courses(request):
    return HttpResponse("Hello, Events and Courses!")


def events_and_courses(request):
    events = Event.objects.all()
    courses = Course.objects.all()
    communities = Community.objects.all()
    interests = Interests.objects.all()
    selected_interest = None

    if request.method == 'GET' and 'interest' in request.GET:
        selected_interest_id = request.GET.get('interest')
        if selected_interest_id:
            selected_interest = get_object_or_404(Interests, pk=selected_interest_id)
            courses = courses.filter(interests=selected_interest)
            events = events.filter(interests=selected_interest)
            communities = communities.filter(interests=selected_interest)
        else:
            selected_interest = None

    context = {
        'courses': courses,
        'events': events,
        'communities': communities,
        'interests': interests,
        'selected_interest': selected_interest,
    }
    
    query = request.GET.get('q')
    if query:
        filtered_events = events.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        filtered_courses = courses.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        filtered_communities = communities.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        context.update({
            'events': filtered_events,
            'courses': filtered_courses,
            'communities': filtered_communities,
            'query': query,
        })
        if not (filtered_events.exists() or filtered_courses.exists() or filtered_communities.exists()):
            messages.info(request, "No results found.")
    return render(request, 'events/events_and_courses.html', context)

def course_list(request):
    interests = Interests.objects.all()
    selected_interest = None
    courses = Course.objects.all()

    if request.method == 'GET' and 'interest' in request.GET:
        selected_interest = get_object_or_404(Interests, pk=request.GET['interest'])
        courses = courses.filter(interests=selected_interest)

    context = {
        'courses': courses,
        'interests': interests,
        'selected_interest': selected_interest,
    }
    return render(request, 'events/course_list.html', context)


def event_list(request):
    interests = Interests.objects.all()
    selected_interest = None
    events = Event.objects.all()

    if request.method == 'GET' and 'interest' in request.GET:
        selected_interest = get_object_or_404(Interests, pk=request.GET['interest'])
        events = events.filter(interests=selected_interest)

    context = {
        'events': events,
        'interests': interests,
        'selected_interest': selected_interest,
    }
    return render(request, 'events/event_list.html', context)


def community_list(request):
    interests = Interests.objects.all()
    selected_interest = None
    communities = Community.objects.all()

    if request.method == 'GET' and 'interest' in request.GET:
        selected_interest = get_object_or_404(Interests, pk=request.GET['interest'])
        communities = communities.filter(interests=selected_interest)

    context = {
        'communities': communities,
        'interests': interests,
        'selected_interest': selected_interest,
    }
    return render(request, 'events/community_list.html', context)

