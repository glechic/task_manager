import json

from django.contrib.auth.models import Group
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from task_manager.models import User, Project, Task


class CommonTestCase(APITestCase):

    def setUp(self):
        self.dev_data = { 'username': 'test_dev', 'password': 'dev1234' }
        self.man_data = { 'username': 'test_man', 'password': 'man1234' }
        self.dev = User.objects.create_user(**self.dev_data)
        self.man = User.objects.create_user(**self.man_data)
        self.dev.groups.add(Group.objects.get(name='developer'))
        self.man.groups.add(Group.objects.get(name='manager'))
        self.dev_token = Token.objects.create(user=self.dev)
        self.man_token = Token.objects.create(user=self.man)

    def tearDown(self):
        self.dev.delete()
        self.man.delete()
        self.dev_token.delete()
        self.man_token.delete()

    def api_authorization(self, token):
        return self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')


class UserLoginAPIViewTestCase(CommonTestCase):
    url = reverse('login')
    
    def test_authorization_without_password(self):
        response = self.client.post(self.url, {'username': self.dev_data['username']})
        self.assertEqual(400, response.status_code)

    def test_authorization_with_wrong_password(self):
        data = self.dev_data.copy()
        data['password'] = 'INVALID'
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_authorization_with_valid_password(self):
        response = self.client.post(self.url, self.dev_data)
        content = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue('token' in content)
        self.assertEqual(content['token'], self.dev_token.key)


class ProjectsAPIViewTestCase(CommonTestCase):
    url = reverse('task_manager:project-list')

    def test_dev_have_safe_only_operations(self):
        self.api_authorization(self.dev_token)

        # list
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        # create
        data = {
            "title": "test_project",
            "member": [1]
        }
        response = self.client.post(self.url, data)
        self.assertEqual(403, response.status_code)

    def test_manager_operations(self):
        self.api_authorization(self.man_token)

        # list
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        # create
        data = {
            "title": "test_project",
            "member": [1]
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)
        self.assertTrue(set(data).issubset(set(json.loads(response.content))))


class TasksAPIViewTestCase(CommonTestCase):
    url = reverse('task_manager:task-list')

    def test_dev_have_safe_only_operations(self):
        pass

    def test_manager_operations(self):
        pass

    def test_dev_can_change_status(self):
        pass 
