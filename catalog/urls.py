from django.conf.urls.static import static
from django.urls import path

from catalog.views import (
    index,
    PerfumeListView,
    PerfumeDetailView,
    PerfumeCreateView,
    PerfumeUpdateView,
    PerfumeCategoryListView,
    PerfumeCategoryCreateView,
    PerfumeCategoryUpdateView,
    PerfumeCategoryDeleteView,
    ManufacturerListView,
    ManufacturerDetailView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    test_session_view, PerfumeDeleteView, PerfumeCategoryDetailView,
)
from perfume_corner import settings

urlpatterns = [
    path("", index, name="index"),
    path("perfumes/", PerfumeListView.as_view(), name="perfume-list"),
    path("perfumes/create/", PerfumeCreateView.as_view(), name="perfume-create"),
    path("perfumes/<int:pk>/delete/", PerfumeDeleteView.as_view(), name="perfume-delete"),
    path("perfumes/<int:pk>/", PerfumeDetailView.as_view(), name="perfume-detail"),
    path("perfumes/<int:pk>/update/", PerfumeUpdateView.as_view(), name="perfume-update"),
    path("categories/<int:pk>/", PerfumeCategoryDetailView.as_view(), name="perfume-category-detail"),
    path("categories/", PerfumeCategoryListView.as_view(), name="perfume-category-list"),
    path("categories/create/", PerfumeCategoryCreateView.as_view(), name="perfume-category-create"),
    path("categories/<int:pk>/update/", PerfumeCategoryUpdateView.as_view(), name="perfume-category-update"),
    path("categories/<int:pk>/delete/", PerfumeCategoryDeleteView.as_view(), name="perfume-category-delete"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturers/create/", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/<int:pk>/", ManufacturerDetailView.as_view(), name="manufacturer-detail"),
    path("manufacturers/<int:pk>/update/", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee-create"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "catalog"