from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Interests
from django.db.models import Q

# Create your views here.
def categories(request):
 return HttpResponse("Hello, interests!")

# Display all interests
def interests_list(request):
    """
    Display a list of all interests.

    **Context**

    ``interests``
        All instances of :model:`categories.Interests`.

    **Template:**

    :template:`categories/interests_list.html`
    """
    query = request.GET.get('q')
    if query:
        interests = Interests.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
        )
        if not interests.exists():
            messages.info(self.request,
                          "Entered interest not found.")
    else:
        interests = Interests.objects.all()
    return render(request,
                  'categories/interests_list.html', {'interests': interests, 'query': query})


# Display posts by category
def posts_by_interests(request, interests_id):
    """
    Display all posts under a specific :model:`blog.Interests`.

    **Context**

    ``interests``
        An instance of :model:`categories.Interests`.
    ``courses/events``
        All courses/events linked to the interests.

    **Template:**

    :template:`categories/posts_by_interests.html`
    """
    interests = get_object_or_404(Interests, id=interests_id)
    posts = interests.posts.filter(status='published')
    return render(request,
                  'categories/posts_by_interests.html',
                  {'interests': interests, 'posts': posts})