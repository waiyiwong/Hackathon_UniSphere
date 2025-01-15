from django.shortcuts import render
from django.http import HttpResponse

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
    interests = Interests.objects.all()
    return render(request,
                  'categories/interests_list.html', {'interests': interests})


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