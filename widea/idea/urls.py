from django.urls import path
from .views import IdeaDetailListView, IdeaCreateView

app_name = 'idea'

urlpatterns = [
    path("idea/<int:pk>/", IdeaDetailListView.as_view(), name="idea_detail"),
    path("idea/new/", IdeaCreateView.as_view(), name = 'idea_new'),
]