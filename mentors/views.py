from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Mentor
from .serializers import MentorSerializer
from django.contrib.auth.models import User

class MentorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({
                "success": False,
                "message": "User with the provided user_id does not exist."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        request.data['user'] = user.id

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                "success": True,
                "message": "Mentor profile created successfully.",
                "mentor_id": serializer.instance.id
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "message": "Invalid data.",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class MentorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]
