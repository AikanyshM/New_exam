from django import forms
from .models import Employee, WorkProject, Membership

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

class WorkProjectForm(forms.ModelForm):
    class Meta:
        model = WorkProject
        fields = "__all__"
        
        
class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = "__all__"
        widgets = {
            'date_joined': forms.widgets.DateInput(attrs={'type': 'date'})
        }