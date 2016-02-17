from django.test import TestCase, Client
from django.core.urlresolvers import reverse


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
        self.assertEqual(len(response.context['person']), 1)


class BadResponse(TestCase):
    def test_404(self):
        """Testing bad response"""
        bad_response = self.client.get('/blah')
        self.assertEqual(bad_response.status_code, 404)
        self.assertTemplateUsed(bad_response, '404.html')