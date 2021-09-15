from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import about, home


class TestUrls(SimpleTestCase):

    def test_about_url(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_home_url(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
