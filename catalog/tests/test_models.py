from django.contrib.auth import get_user_model
from django.test import TestCase

from perfume_corner.models import PerfumeCategory, Manufacturer, Perfume


class ModelTests(TestCase):
    def test_perfume_category_str(self):
        category = PerfumeCategory.objects.create(name="Floral")
        self.assertEqual(str(category), category.name)

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="Test Manufacturer", country="Test Country"
        )
        self.assertEqual(str(manufacturer), f"{manufacturer.name} ({manufacturer.country})")

    def test_perfume_str(self):
        manufacturer = Manufacturer.objects.create(
            name="Test Manufacturer", country="Test Country"
        )
        category = PerfumeCategory.objects.create(name="Floral")
        perfume = Perfume.objects.create(
            name="Test Perfume", manufacturer=manufacturer, category=category
        )
        self.assertEqual(
            str(perfume), f"{perfume.name} ({perfume.manufacturer.name})"
        )

    def test_create_employee_with_position(self):
        username = "test_employee"
        password = "employee123"
        position = "Manager"
        employee = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name="Test",
            last_name="Employee",
            position=position,
        )
        self.assertEqual(employee.username, username)
        self.assertEqual(employee.position, position)
        self.assertTrue(employee.check_password(password))
