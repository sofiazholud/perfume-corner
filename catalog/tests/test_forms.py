from django.test import TestCase
from perfume_corner.forms import EmployeeCreationForm, PerfumeForm
from perfume_corner.models import Manufacturer


class FormTests(TestCase):
    def test_employee_creation_form_is_valid(self):
        form_data = {
            "username": "new_employee",
            "password1": "employee12test",
            "password2": "employee12test",
            "first_name": "Employee First",
            "last_name": "Employee Last",
            "position": "Manager",
        }
        form = EmployeeCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "new_employee")

    def test_perfume_creation_form_is_valid(self):
        manufacturer = Manufacturer.objects.create(
            name="Test Manufacturer",
            country="Test Country"
        )
        form_data = {
            "name": "Test Perfume",
            "category": "Floral",
            "manufacturer": manufacturer.id,
            "notes": "Citrus, Rose, Amber"
        }
        form = PerfumeForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Test Perfume")
