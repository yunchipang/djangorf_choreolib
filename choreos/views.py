from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer, UserSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions
from choreos.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'choreos': reverse('choreography-list', request=request, format=format)
    })

class ChoreographyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChoreographyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer