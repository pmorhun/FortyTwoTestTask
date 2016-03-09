from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from apps.contact.models import Person


class PersonViewTest(TestCase):
    def test_contact(self):
        """Testing response view"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        data = Person.objects.get(id=1)
        self.assertContains(response, data.first_name)
        self.assertContains(response, data.last_name)
        self.assertContains(response, date(data.birthday))
        self.assertContains(response, data.email)
        self.assertContains(response, data.skype)
        self.assertContains(response, data.jabber)
        self.assertContains(response, data.bio)
        self.assertContains(response, data.other_contacts)
        count = Person.objects.all().count()
        self.assertEqual(count, 1)


class BadResponse(TestCase):
    def test_404(self):
        """Testing bad response"""
        bad_response = self.client.get('/blah')
        self.assertEqual(bad_response.status_code, 404)
        self.assertTemplateUsed(bad_response, '404.html')


class PersonModelTests(TestCase):
    def test_unicode(self):
        """Test person model"""
        person = Person(first_name='Test', last_name='Testerenko')
        self.assertEqual(unicode(person), u'Test Testerenko')


class ContactFormTest(TestCase):

    def setUp(self):
        Person.objects.update(
            first_name="Tester",
            last_name="Testerenko",
            birthday="2011-01-01",
            email="test@test.com",
            photo="test.jpg")

        # remember test browser
        self.client = Client()
        # remember url to edit form
        self.url = reverse('edit_person')

    def test_form(self):
        """test fields of form"""
        # get form and check few fields there
        response = self.client.get(self.url)
        # check response status
        self.assertEqual(response.status_code, 200)
        # check page title, few field titles and button on edit form
        self.assertIn('First name', response.content)
        self.assertIn('Email', response.content)
        self.assertIn('Last name', response.content)
        self.assertIn('value="Save"', response.content)
        self.assertIn('Cancel', response.content)
        self.assertIn('action="%s"' % self.url, response.content)
        self.assertIn('test.jpg', response.content)

    def test_success_post(self):
        """test post form with valid data"""
        response = self.client.post(self.url, {'first_name': 'Upd Name',
                                               'last_name': 'Upd Last Name',
                                               'email': 'upd@test.com',
                                               "jabber": "pm@42cc.co",
                                               "bio": "blah, blah...",
                                               "other_contacts": "blah...",
                                               "birthday": "1999-11-11",
                                               "skype": "p.etros",
                                               },
                                    follow=True)
        # check response status
        self.assertEqual(response.status_code, 200)
        # test updated person details
        person = Person.objects.get(pk=1)

        self.assertEqual(person.first_name, 'Upd Name')
        self.assertEqual(person.last_name, 'Upd Last Name')
        self.assertEqual(person.email, 'upd@test.com')
