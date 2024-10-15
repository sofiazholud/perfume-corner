from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class PerfumeCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Perfume(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        PerfumeCategory,
        on_delete=models.CASCADE,
        related_name="perfumes",
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="perfumes"
    )
    notes = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} ({self.manufacturer.name})"

    def get_absolute_url(self):
        return reverse("perfume-detail", args=[str(self.id)])


class Employee(AbstractUser):
    position = models.CharField(max_length=63, null=True, blank=True)
    favorite_perfumes = models.ManyToManyField(Perfume, related_name="liked_by")

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("employee-detail", args=[str(self.id)])
