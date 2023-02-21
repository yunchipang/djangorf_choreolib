from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer

from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics


class ChoreographyList(mixins.ListModelMixin,
                       mixins.CreateModelMixin, 
                       generics.GenericAPIView):
    """
    List all choreographies, or create a new choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ChoreographyDetail(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    """
    Retrieve, update or delete a choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)