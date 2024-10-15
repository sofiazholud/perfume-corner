from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from perfume_corner.models import Perfume, Manufacturer


class AdminSiteTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)

        self.manufacturer = Manufacturer.objects.create(
            name="Test Manufacturer",
            country="Test Country"
        )

        self.perfume = Perfume.objects.create(
            name="Test Perfume",
            manufacturer=self.manufacturer
        )

    def test_perfume_name_listed(self):
        """
        Test that perfume's name is in list_display on perfume admin page
        """
        url = reverse("admin:perfume_corner_perfume_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.perfume.name)

    def test_perfume_detail_manufacturer_listed(self):
        """
        Test that perfume's manufacturer is on perfume detail admin page
        """
        url = reverse("admin:perfume_corner_perfume_change", args=[self.perfume.id])
        res = self.client.get(url)
        self.assertContains(res, self.perfume.manufacturer.name)
