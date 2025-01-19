from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Course, Event, Community, Rating, Ticket
from .forms import CourseForm, EventForm, CommunityForm, TicketForm, CourseEditForm, RatingForm
from categories.models import Interests
from django.db.models import Q
from django.contrib import messages
from django.db.models import Avg

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
    
    for event in events:
        # Calculate the average rating for the event
        average_rating = event.ratings.aggregate(Avg('rating'))['rating__avg'] or 0.0
        event.average_rating = average_rating
        event.user_has_approved_ticket = Ticket.objects.filter(ticket_holder=request.user, event=event, approved=True).exists()

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

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def manage_items(request):
    """
    View for Events Organisers to manage (add, edit, delete) courses, events, and communities.
    """
    courses = Course.objects.all()
    events = Event.objects.all()
    communities = Community.objects.all()
    tickets = Ticket.objects.all()

    course_form = CourseForm()
    event_form = EventForm()
    community_form = CommunityForm()
    ticket_form = TicketForm()

    if request.method == 'POST':
        if 'create_course' in request.POST:
            course_form = CourseForm(request.POST)
            if course_form.is_valid():
                course_form.save()
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Course creation successfull!')
                return redirect('manage_items')

        if 'create_event' in request.POST:
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event_form.save()
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Event creation successfull!')
                return redirect('manage_items')

        if 'create_community' in request.POST:
            community_form = CommunityForm(request.POST)
            if community_form.is_valid():
                community_form.save()
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Community creation successfull!')
                return redirect('manage_items')
        
        if 'create_ticket' in request.POST:
            ticket_form = TicketForm(request.POST)
            if ticket_form.is_valid():
                ticket_form.save()
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Ticket creation successfull!')
                return redirect('manage_items')

    context = {
        'courses': courses,
        'events': events,
        'communities': communities,
        'tickets': tickets,
        'course_form': course_form,
        'event_form': event_form,
        'community_form': community_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'events/manage_items.html', context)

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('manage_items')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Course edit successfull!')
            return redirect('manage_items')
    else:
        form = CourseForm(instance=course)
    return render(request, 'events/edit_item.html', {'form': form, 'item_type': 'Course'})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Course delete successfull!')
    return redirect('manage_items')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Event edit successfull!')
            return redirect('manage_items')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_item.html', {'form': form, 'item_type': 'Event'})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Event delete successfull!')
    return redirect('manage_items')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def edit_community(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()
            messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Community edit successfull!')
            return redirect('manage_items')
    else:
        form = CommunityForm(instance=community)
    return render(request, 'events/edit_item.html', {'form': form, 'item_type': 'Community'})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def delete_community(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    community.delete()
    messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Community delete successfull!')
    return redirect('manage_items')

@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Ticket edit successfull!')
            return redirect('manage_items')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'events/edit_item.html', {'form': form, 'item_type': 'Ticket'})


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Events Organiser').exists())
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Ticket delete successfull!')
    return redirect('manage_items')

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)

def request_to_join_e(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user.is_authenticated:
        messages.success(request, 'Request received. A confirmation will be sent once enrolled.')
    else:
        messages.error(request, 'Please log in to request to join an event.')
    return redirect('eventsandcourses')

def request_to_join_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.user.is_authenticated:
        messages.success(request, 'Request received. A confirmation will be sent once enrolled.')
    else:
        messages.error(request, 'Please log in to request to join a course.')
    return redirect('eventsandcourses')

def request_to_join_com(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.user.is_authenticated:
        messages.success(request, 'Request received. A confirmation will be sent by the organiser.')
    else:
        messages.error(request, 'Please log in to request to join a community.')
    return redirect('eventsandcourses')
