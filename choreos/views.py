from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer
from rest_framework import generics


class ChoreographyList(generics.ListCreateAPIView):
    """
    List all choreographies, or create a new choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer

class ChoreographyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a choreography.
    """
    queryset = Choreography.objects.all()
    serializer_class = ChoreographySerializer