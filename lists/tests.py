from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


# Create your tests here.
class SmokeTest(TestCase):

    def test_when_root_url_then_goto_the_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
