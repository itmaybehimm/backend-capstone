from django.test import TestCase
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        # Creating test instances of the Menu model
        self.menu1 = MenuItem.objects.create(
            title='Menu 1', inventory=1, price=10.99)
        self.menu2 = MenuItem.objects.create(
            title='Menu 2', inventory=2, price=15.99)
        # Add more instances if needed for testing

    def test_getall(self):
        # Retrieving all Menu objects
        menus = MenuItem.objects.all()

        # Serializing the retrieved objects using MenuItemSerializer
        serialized_menus = MenuItemSerializer(menus, many=True).data

        # Checking if the serialized data equals the response
        relevant_data = [{'title': menu['title'], 'inventory': menu['inventory'],
                          'price': menu['price']} for menu in serialized_menus]

        # Expected data in the same format
        expected_data = [
            {'title': 'Menu 1', 'inventory': 1, 'price': '10.99'},
            {'title': 'Menu 2', 'inventory': 2, 'price': '15.99'},
            # Add more expected data based on the test instances added in setUp
        ]

        # Asserting if the serialized data matches the expected data
        self.assertEqual(relevant_data, expected_data)
