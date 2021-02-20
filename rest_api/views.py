from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import TaskSerializer
from .models import Task


# Create your views/api endpoint here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_overview(request):
    """this view is just meant to be an overview
    """
    api_urls = {
        'list': 'test'
    }

    return Response(api_urls)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def task_list(request):
    tasks = Task.objects.all()

    # returns all objects
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)

    # returns only 1 object
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)
