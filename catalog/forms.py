from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Perfume, Manufacturer, Employee


class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "position",)


class PerfumeForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        widget=forms.RadioSelect(),
        required=True,
    )
    class Meta:
        model = Perfume
        fields = "__all__"


class PerfumeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by perfume name"
            }
        ),
    )

class ManufacturerSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by manufacturer name"
            }
        ),
    )

class EmployeeSearchForm(forms.Form):
    search = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Search by name...',
        'class': 'form-control'
    }))