from django.test import SimpleTestCase

from django.urls import reverse
# Create your tests here.


class ThingsTests(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
