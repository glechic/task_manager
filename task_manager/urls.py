from rest_framework.routers import SimpleRouter

from .views import ProjectViewSet, TaskViewSet, DeveloperViewSet

app_name = 'task_manager'

router = SimpleRouter()
for url, view, name in zip(
        ['developers', 'projects', 'tasks'],
        [DeveloperViewSet, ProjectViewSet, TaskViewSet],
        ['developer', 'project', 'task']):
    router.register(url, view, basename=name)

urlpatterns = router.urls
