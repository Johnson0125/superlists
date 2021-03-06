from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


# Create your tests here.
class SmokeTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second (ever) list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_save_item = saved_items[0]
        second_save_item = saved_items[1]

        self.assertEqual(first_save_item.text, 'The first (ever) list item')
        self.assertEqual(second_save_item.text, 'The second (ever) list item')