from django.shortcuts import render
from myapp.models import Posts

# Create your views here.
def index(request):
    ourposts = Posts.objects.all()
    the_posts =   {'key': ourposts}  
    return render(request, 'index.html', context = the_posts)