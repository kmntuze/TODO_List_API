
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoAPITests(APITestCase):
    def setUp(self):
        self.list_url = reverse('list_create_todo')

    def test_create_todo(self):
        data = {
            'title': 'Test todo',
            'description': 'Testing create',
            'is_completed': False
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.first().title, 'Test todo')

    def test_list_todos(self):
        Todo.objects.create(title='First todo')
        Todo.objects.create(title='Second todo')

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_todo(self):
        todo = Todo.objects.create(title='Single todo')

        response = self.client.get(reverse('todo_detail', args=[todo.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Single todo')

    def test_update_todo(self):
        todo = Todo.objects.create(title='Old title')

        data = {
            'title': 'New title',
            'description': 'Updated description',
            'is_completed': True
        }

        response = self.client.put(
            reverse('todo_detail', args=[todo.id]),
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'New title')
        self.assertTrue(todo.is_completed)

    def test_patch_todo(self):
        todo = Todo.objects.create(title='Patch me', is_completed=False)

        response = self.client.patch(
            reverse('todo_detail', args=[todo.id]),
            {'is_completed': True},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title='Delete me')

        response = self.client.delete(reverse('todo_detail', args=[todo.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

    def test_missing_title_returns_400(self):
        data = {
            'description': 'No title here',
            'is_completed': False
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_blank_title_returns_400(self):
        data = {
            'title': '   ',
            'description': 'Blank title',
            'is_completed': False
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_todo_returns_404(self):
        response = self.client.get(reverse('todo_detail', args=[999]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
