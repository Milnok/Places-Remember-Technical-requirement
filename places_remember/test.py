from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.test.client import RequestFactory
from .models import Place
from .forms import PlaceForm
from .views import MyMemories, CreateMemory


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('user123', 'pavel@mail.ru', 'qwerty')
        self.factory = RequestFactory()

    def test_my_memories(self):
        self.client.login(username='user123', password='qwerty')
        request = self.factory.get('/my_memories')
        request.user = self.user
        response = MyMemories.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_create_memory_view(self):
        self.client.login(username='user123', password='qwerty')
        request = self.factory.get('/create_memory')
        request.user = self.user
        response = CreateMemory.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_create_memory_object(self):
        place_data = {
            'title': 'title2',
            'discription': 'discription2',
            'coords': '15,15',
        }
        place_form = PlaceForm(place_data)

        request = self.factory.post('/create_memory', place_data)
        request.user = self.user
        CreateMemory.as_view()(request)

        self.assertEqual(Place.objects.get(pk=1).title, 'title2')
