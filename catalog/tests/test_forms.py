from django.test import TestCase
from catalog.forms import (EmployeeCreationForm, PerfumeForm)
from catalog.models import Manufacturer, PerfumeCategory


class FormTests(TestCase):
    def test_employee_creation_form_is_valid(self):
        form_data = {
            'username': 'new_employee',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'Employee First',
            'last_name': 'Employee Last',
            'position': 'Manager',
            'email': 'new_employee@example.com'
        }
        form = EmployeeCreationForm(data=form_data)

        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid())

    def test_perfume_creation_form_is_valid(self):
        manufacturer = Manufacturer.objects.create(
            name='Test Manufacturer',
            country='Test Country'
        )
        category = PerfumeCategory.objects.create(name='Floral')

        form_data = {
            'name': 'Test Perfume',
            'category': category.id,
            'manufacturer': manufacturer.id,
            'notes': 'Citrus, Rose, Amber'
        }
        form = PerfumeForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
