from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse


class PerfumeCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(
        max_length=63,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.country})'


class Perfume(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        PerfumeCategory,
        on_delete=models.CASCADE,
        related_name='perfumes',
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='perfumes'
    )
    notes = models.TextField(null=True, blank=True)

    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.manufacturer.name})'

    def get_absolute_url(self):
        return reverse('perfume-detail', args=[str(self.id)])


class EmployeeManager(BaseUserManager):
    def create_user(
        self,
            username,
            email=None,
            password=None,
            position=None,
            **extra_fields
    ):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            position=position,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username,
            email=None,
            password=None,
            position=None,
            **extra_fields
    ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            username,
            email,
            password,
            position,
            **extra_fields
        )


class Employee(AbstractUser):
    position = models.CharField(
        max_length=63,
        null=True,
        blank=True
    )
    favorite_perfumes = models.ManyToManyField(
        Perfume,
        related_name='liked_by'
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    objects = EmployeeManager()

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'

    def get_absolute_url(self):
        return reverse(
            'employee-detail',
            args=[str(self.id)])
