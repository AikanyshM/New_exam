from django.contrib import admin
from .models import Employee, Passport, WorkProject, Membership, Client, VIPClient
from datetime import date
from .forms import EmployeeForm




@admin.display(description='experience_year')
def get_experience_year(obj):
    experience_year = date.today().year - experience_year.year
    return experience_year

def get_button(obj): 
    return "Подробнее"

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    list_display = ('name', 'work_position', get_experience_year, get_button)
    search_fields = ('name',)
    list_display_links = (get_button,)


class PassportAdmin(admin.ModelAdmin):
    list_display = ('employee.name', 'inn', 'card_id')




admin.site.register(Employee, EmployeeAdmin)