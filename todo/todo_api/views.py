from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .serializers import TaskSerializers


class TaskListApiView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        new_task = {
            "title" : request.data.get('title'),
            "done" : False
        }

        serializer = TaskSerializers(data=new_task)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

