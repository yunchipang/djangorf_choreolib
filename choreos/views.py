from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from choreos.models import Choreography
from choreos.serializers import ChoreographySerializer


@csrf_exempt
def choreographies_list(request):
    """
    List all choreographies, or create a new choreography.
    """
    if request.method == 'GET':
        choreographies = Choreography.objects.all()
        serializer = ChoreographySerializer(choreographies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChoreographySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def choreography_detail(request, pk):
    """
    Retrieve, update or delete a choreography.
    """
    try:
        choreography = Choreography.objects.get(pk=pk)
    except Choreography.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChoreographySerializer(choreography)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChoreographySerializer(choreography, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        choreography.delete()
        return HttpResponse(status=204)