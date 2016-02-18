from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from apps.hello.models import Person


class PersonViewTest(TestCase):

    def test_hello(self):
        """Testing response view"""
        response = self.client.get(reverse('person'))
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
