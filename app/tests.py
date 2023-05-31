from django.test import TestCase
from django.urls import resolve, reverse
from .views import *

class UrlTest(TestCase):

    def test_urls(self):
        url = reverse('admin-dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, admin_dashboard)