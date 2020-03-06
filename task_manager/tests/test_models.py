from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

from task_manager.models import Project, Task


class ModelsTests(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.task1 = Task.objects.get(pk=1)
        self.proj1 = Project.objects.get(pk=1)
        self.mans = Group.objects.get(name='manager')
        self.devs = Group.objects.get(name='developer')

    def test_simple_models_tester(self):
        self.assertIn(self.mans, self.user1.groups.all())
        self.assertIn(self.devs, self.user2.groups.all())

    def test_correctly_assogned_owner(self):
        self.user2.project_set.clear()  # Now user2 don't assign to any project
        self.task1.owner = self.user2
        self.assertRaises(ValidationError, callable=self.task1.full_clean)
