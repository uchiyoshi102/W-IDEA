from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Idea

# Create your views here.

class IdeaListView(ListView):
    model = Idea
    template_name = 'idea/home_idea.html'

class IdeaDetailListView(DetailView):
    model = Idea
    template_name = 'idea/idea_detail.html'
    
class IdeaCreateView(CreateView):
   model = Idea
   template_name = 'idea/idea_new.html'
   fields = ['title', 'author', 'body']