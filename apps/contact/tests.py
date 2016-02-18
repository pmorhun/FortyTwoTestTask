from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from apps.contact.models import Person


class PersonViewTest(TestCase):

    def test_contact(self):
        """Testing response view"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

        td = Person.objects.get()
        self.assertContains(response, td.first_name)
        self.assertContains(response, td.last_name)
        self.assertContains(response, date(td.birthday))
        self.assertContains(response, td.bio)
        self.assertContains(response, td.email)
        self.assertContains(response, td.jabber)
        self.assertContains(response, td.skype)
        self.assertContains(response, td.other_contacts)


class BadResponse(TestCase):
    def test_404(self):
        """Testing bad response"""
        bad_response = self.client.get('/blah')
        self.assertEqual(bad_response.status_code, 404)
        self.assertTemplateUsed(bad_response, '404.html')
