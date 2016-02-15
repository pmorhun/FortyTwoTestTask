from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from apps.hello.models import Person


class PersonViewTest(TestCase):
    fixtures = ['init_data.json']

    def test_hello(self):
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

    def test_404(self):
        bad_response = self.client.get('/blah')
        self.assertEqual(bad_response.status_code, 404)
        self.assertTemplateUsed(bad_response, '404.html')
