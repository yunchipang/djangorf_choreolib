from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def choreographies_list(request, format=None):
    """
    List all choreographies, or create a new choreography.
    """
    if request.method == 'GET':
        choreographies = Choreography.objects.all()
        serializer = ChoreographySerializer(choreographies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChoreographySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def choreography_detail(request, pk, format=None):
    """
    Retrieve, update or delete a choreography.
    """
    try:
        choreography = Choreography.objects.get(pk=pk)
    except Choreography.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChoreographySerializer(choreography)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChoreographySerializer(choreography, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        choreography.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)