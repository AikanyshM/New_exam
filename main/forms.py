from django import forms
from .models import Employee, Passport, WorkProject, Membership, Client, VIPClient


class EmployeeForm(forms.ModelForm):
    class Meta:
        widgets = {
            'experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
