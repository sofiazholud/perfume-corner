from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import PerfumeCategory, Perfume, Manufacturer

PERFUME_CATEGORY_URL = reverse('catalog:perfume-category-list')


class PublicPerfumeCategoryTest(TestCase):
    def test_login_required(self):
        """Test that login is required for accessing perfume categories"""
        res = self.client.get(PERFUME_CATEGORY_URL)
        self.assertEqual(res.status_code, 302)  # Redirect to login page


class PrivatePerfumeCategoryTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='test123',
        )
        self.client.force_login(self.user)

    def test_retrieve_perfume_category(self):
        """Test that perfume categories can be retrieved for logged in users"""
        PerfumeCategory.objects.create(name='Floral')
        PerfumeCategory.objects.create(name='Citrus')
        response = self.client.get(PERFUME_CATEGORY_URL)

        self.assertEqual(response.status_code, 200)
        perfume_categories = PerfumeCategory.objects.all()
        self.assertEqual(
            list(response.context['perfume_category_list']),
            list(perfume_categories),
        )
        self.assertTemplateUsed(response, 'catalog/perfume_category_list.html')


class PrivatePerfumeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='test',
            password='password123',
        )
        self.client.force_login(self.user)

    def test_create_perfume(self):
        """Test creating a new perfume"""
        category_new = PerfumeCategory.objects.create(name='Floral')
        manufacturer = Manufacturer.objects.create(
            name='Test Manufacturer',
            country='Test Country'
        )
        form_data = {
            'name': 'Test Perfume',
            'manufacturer': manufacturer.id,
            'category': category_new.id,
            'notes': 'Citrus, Jasmine, Amber',
        }
        self.client.post(reverse('catalog:perfume-create'), data=form_data)
        perfume = Perfume.objects.get(name=form_data['name'])

        self.assertEqual(perfume.name, form_data['name'])
        self.assertEqual(perfume.notes, form_data['notes'])
