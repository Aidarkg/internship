from aidar.serializers import TaskSerializer
from aidar.models import Task
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'