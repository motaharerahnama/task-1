# mentors/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from mentors.models import Mentor
from mentors.serializers import MentorSerializer
from django.conf import settings


class MentorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mentor = serializer.save()
            return Response({
                "success": True,
                "message": "Mentor profile created successfully.",
                "mentor_id": mentor.id
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "message": "Invalid user ID or missing data."
            }, status=status.HTTP_400_BAD_REQUEST)

class MentorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]
