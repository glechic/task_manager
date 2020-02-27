from rest_framework import viewsets

from .serializers import ProjectSerializer, TaskSerializer, UserSerializer
from .models import Task, User, Project


class DeveloperViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(groups__name='developer')


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
