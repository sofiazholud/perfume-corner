from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from . import forms
from .models import Perfume, Manufacturer, PerfumeCategory, Employee

from .forms import EmployeeCreationForm, PerfumeSearchForm, PerfumeForm, ManufacturerSearchForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_perfumes = Perfume.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_categories = PerfumeCategory.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_perfumes": num_perfumes,
        "num_manufacturers": num_manufacturers,
        "num_categories": num_categories,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=context)


class PerfumeListView(LoginRequiredMixin, generic.ListView):
    model = Perfume
    template_name = "catalog/perfume_list.html"
    context_object_name = "perfume_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = PerfumeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Perfume.objects.select_related("category", "manufacturer")
        form = PerfumeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class PerfumeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Perfume
    form_class = PerfumeForm
    success_url = reverse_lazy("catalog:perfume-list")


class PerfumeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Perfume
    form_class = PerfumeForm
    success_url = reverse_lazy("catalog:perfume-list")

class PerfumeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Perfume
    success_url = reverse_lazy("catalog:perfume-list")



class PerfumeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Perfume
    template_name = "catalog/perfume_detail.html"
    context_object_name = "perfume"



class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "catalog/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = ManufacturerSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Manufacturer.objects.all()
        form = ManufacturerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("catalog:manufacturer-list")


class ManufacturerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manufacturer


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("catalog:manufacturer-list")


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = "catalog/employee_list.html"
    context_object_name = "employee_list"
    paginate_by = 5


class EmployeeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeCreationForm
    success_url = reverse_lazy("catalog:employee-list")


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee


class PerfumeCategoryListView(LoginRequiredMixin, generic.ListView):
    model = PerfumeCategory
    template_name = "catalog/perfume_category_list.html"
    context_object_name = "perfume_category_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def test_session_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "<h1>Test session</h1>",
        f"<h4>Session data: {request.session['num_visits']}</h4>"
    )


class PerfumeCategoryCreateView(CreateView):
    model = PerfumeCategory
    fields = ["name"]
    success_url = reverse_lazy("catalog:perfume-list")
    template_name = "catalog/perfume_category_form.html"

class PerfumeCategoryUpdateView(UpdateView):
    model = PerfumeCategory
    fields = ['name']
    template_name = 'catalog/perfume_category_form.html'
    success_url = reverse_lazy('catalog:perfume-category-list')

class PerfumeCategoryDeleteView(DeleteView):
    model = PerfumeCategory
    template_name = 'catalog/perfume_category_confirm_delete.html'
    success_url = reverse_lazy('catalog:perfume-category-list')

class PerfumeCategoryDetailView(DetailView):
    model = PerfumeCategory
    template_name = "catalog/perfume_category_detail.html"
    context_object_name = "category"

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(context['perfume_category_list'])
    return context