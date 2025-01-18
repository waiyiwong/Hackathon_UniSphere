from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages


# Create your views here.


@login_required
def profile(request):
    """View to display a user's profile to edit."""
    profile, created = Profile.objects.get_or_create(user=request.user)

    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(
            request, 
            messages.SUCCESS,
            'Your profile has been edited!'
    )
            print(redirect('view_profile', username=request.user.username))
            return redirect('view_profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        
    }
    return render(request, 'user_account/profile.html', context)

def view_profile(request, username):
    """View to display a user's profile."""

    has_permission = request.user.groups.filter(name='Events Organiser').exists()
    print('has_permission', has_permission)

    user_profile = get_object_or_404(Profile, user__username=username)
    context = {
        'profile': user_profile,
        'has_permission': has_permission
    }
    return render(request, 'user_account/view_profile.html', context)