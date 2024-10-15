from django.contrib import admin
from .models import Perfume, Manufacturer, PerfumeCategory, Employee


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "manufacturer", "notes"]
    list_filter = ["category", "manufacturer"]
    search_fields = ["name", "manufacturer__name", "notes"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name", "country"]


@admin.register(PerfumeCategory)
class PerfumeCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position')

