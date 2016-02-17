from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from apps.hello.models import Person


class TestPersonView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('person')

    def test_person_hard(self):
        """test view with in view"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('Petro', response.content)
        self.assertIn('p.etros', response.content)
        self.assertEqual(len(response.context['persons']), 1)


class PersonViewTest(TestCase):
    fixtures = ['init_data.json']

    def test_hello(self):
        """Testing response view"""
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)

        data = Person.objects.get()
        self.assertContains(response, data.first_name)
        self.assertContains(response, data.last_name)
        self.assertContains(response, date(data.birthday))
        self.assertContains(response, data.bio)
        self.assertContains(response, data.email)
        self.assertContains(response, data.jabber)
        self.assertContains(response, data.skype)
        self.assertContains(response, data.contacts)


class BadResponse(TestCase):
    def test_404(self):
        """Testing bad response"""
        bad_response = self.client.get('/blah')
        self.assertEqual(bad_response.status_code, 404)
        self.assertTemplateUsed(bad_response, '404.html')
