from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from .models import RequestsLog


class RequestLogTest(TestCase):
    def setUp(self):
        RequestsLog.objects.create(url='/test', method="post")

    def test_hello(self):
        """Testing response view RequestLogView"""
        response = self.client.get(reverse('all_requests'))
        self.assertEqual(response.status_code, 200)

        data = RequestsLog.objects.all()[0]
        self.assertContains(response, data.url)
        self.assertContains(response, data.method)
        self.assertContains(response, date(data.date))

    def test_count_record_in_db(self):
        """Testing count record in db"""
        count_before = RequestsLog.objects.count()
        self.client.get(reverse('contact'))
        count_after = RequestsLog.objects.count()
        self.assertEqual(count_after, count_before + 1)
