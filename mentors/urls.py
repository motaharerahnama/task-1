# mentors/urls.py

from django.urls import path
from .views import MentorListCreateAPIView, MentorDetailAPIView

urlpatterns = [
    path('', MentorListCreateAPIView.as_view(), name='mentor-list-create'),
    path('<int:pk>/', MentorDetailAPIView.as_view(), name='mentor-detail'),
]
