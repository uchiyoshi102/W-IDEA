from django.urls import path
from .views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView

urlpatterns = [
  path("", TopicListView.as_view(), name="home_topic"),
  path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
  path("topic/new/", TopicCreateView.as_view(), name = "topic_new"),
  path("topic/<int:pk>/edit/", TopicUpdateView.as_view(), name = "topic_edit"),
  path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name = "topic_delete"),
]