from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer

from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class ChoreographyList(APIView):
    """
    List all choreographies, or create a new choreography.
    """
    def get(self, request, format=None):
        choreographies = Choreography.objects.all()
        serializer = ChoreographySerializer(choreographies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoreographySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChoreographyDetail(APIView):
    """
    Retrieve, update or delete a choreography.
    """
    def get_object(self, pk):
        try:
            return Choreography.objects.get(pk=pk)
        except Choreography.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        choreography = self.get_object(pk)
        serializer = ChoreographySerializer(choreography)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        choreography = self.get_object(pk)
        serializer = ChoreographySerializer(choreography, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        choreography = self.get_object(pk)
        choreography.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)