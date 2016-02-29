from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import RequestsLog


class RequestLogTest(TestCase):
    def setUp(self):
        RequestsLog.objects.create(path='/test', method="post")

    def test_requests(self):
        """Testing response view RequestLogView"""
        response = self.client.get(reverse('requests_list'))
        self.assertEqual(response.status_code, 200)

    def test_count_record_in_db(self):
        """Testing count record in db"""
        count_before = RequestsLog.objects.count()
        self.client.get(reverse('contact'))
        count_after = RequestsLog.objects.count()
        self.assertEqual(count_after, count_before + 1)
