from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


# Create your tests here.
class SmokeTest(TestCase):

    def test_when_root_url_then_goto_the_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_when_home_page_then_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_given_client_when_home_page_then_correct(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')