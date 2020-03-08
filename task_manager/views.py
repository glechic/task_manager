from rest_framework import viewsets

from .permissions import ManagerPermission, DeveloperPermission, DeveloperTaskPermission
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer
from .models import Task, User, Project


class DeveloperViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(groups__name='developer')
    permission_classes = [ManagerPermission|DeveloperPermission]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [ManagerPermission|DeveloperTaskPermission]


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [ManagerPermission|DeveloperPermission]
