from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer, UserSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework import status


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'choreos': reverse('choreography-list', request=request, format=format)
    })


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        # get username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')
        
        # create new user object
        user = User.objects.create_user(username=username, password=password)
        
        # return success response
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    else:
        # return error response for invalid request method
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

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

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
