from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer, UserSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions
from choreos.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'choreographies': reverse('choreography-list', request=request, format=format)
    })

class ChoreographyList(generics.ListCreateAPIView):
    """
    List all choreographies, or create a new choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChoreographyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer