from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Topic

class TopicListView(ListView):
   model = Topic
   template_name = "topic/home_topic.html"
   
class TopicDetailView(DetailView):
   model = Topic
   template_name = "topic/topic_detail.html"
   
class TopicCreateView(CreateView):
   model = Topic
   template_name = "topic/topic_new.html"
   fields = ["title", "author", "body"]
   
class TopicUpdateView(UpdateView):
   model = Topic
   template_name = "topic/topic_edit.html"
   fields = ["title", "body"]
   
class TopicDeleteView(DeleteView):
   model = Topic
   template_name = "topic/topic_delete.html"
   success_url = reverse_lazy("home_topic")
   

