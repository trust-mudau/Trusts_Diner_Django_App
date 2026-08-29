from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import MenuItem


class MenuViewsTests(TestCase):
    def setUp(self):
        self.burger = MenuItem.objects.create(
            name='Classic Burger',
            description='Beef patty with fresh toppings.',
            price=Decimal('89.90'),
        )

    def test_home_lists_menu_items(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.burger.name)
        self.assertContains(response, 'R89.90')

    def test_detail_displays_selected_item(self):
        response = self.client.get(reverse('item_detail', args=[self.burger.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.burger.description)

    def test_missing_item_returns_404(self):
        response = self.client.get(reverse('item_detail', args=[99999]))

        self.assertEqual(response.status_code, 404)

    def test_model_string_uses_name(self):
        self.assertEqual(str(self.burger), 'Classic Burger')
