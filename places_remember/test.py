from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse
from .models import Place
from .views import create_place_obj, get_my_memories_context


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('user123', 'pavel@mail.ru', 'qwerty')
        self.factory = RequestFactory()

        self.place1 = Place.objects.create(
            user=self.user,
            title='title',
            discription='discription',
            latitude='12',
            longitude='12'
        )

        self.place2 = Place.objects.create(
            user=self.user,
            title='title2',
            discription='discription2',
            latitude='15',
            longitude='15'
        )

    def test_my_memories(self):
        self.client.login(username='user123', password='qwerty')
        response = self.client.get(reverse('my_memories'))
        self.assertEqual(response.status_code, 200)

    def test_create_memory(self):
        self.client.login(username='user123', password='qwerty')
        response = self.client.get(reverse('create_memory'))
        self.assertEqual(response.status_code, 200)

    def test_create_place_obj(self):
        request = self.factory.get('create_memory')

        mutable = request.POST._mutable

        request.POST._mutable = True

        request.user = self.user
        request.POST['title'] = 'title'
        request.POST['discription'] = 'discription'
        request.POST['coords'] = '12,12'

        request.POST._mutable = mutable

        place_from_function = create_place_obj(request)

        self.assertEqual(self.place1.title, place_from_function.title)
        self.assertEqual(self.place1.discription, place_from_function.discription)
        self.assertEqual(self.place1.latitude, place_from_function.latitude)
        self.assertEqual(self.place1.longitude, place_from_function.longitude)

    def test_get_my_memories_context(self):
        request = self.factory.get('my_memories')
        request.user = self.user

        context_from_function = get_my_memories_context(request)
        my_context = {'memories': Place.objects.filter(user=request.user)}

        self.assertQuerysetEqual(context_from_function['memories'], my_context['memories'], ordered=False)
