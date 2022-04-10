from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Employee, Passport, WorkProject, Membership, Client, VIPClient
from .forms import EmployeeForm, WorkProjectForm, MembershipForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'

def get_queryset(request):
        name = request.GET.get('query')
        queryset = Employee.objects.all()

        if name or name != '':
            queryset = queryset.filter(name__icontains=name)
        else:
            queryset = Employee.objects.all()
        return queryset


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['membership'] = Membership.objects.filter(employee=self.get_object())
        return context


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'

class WorkProjectListView(ListView):
    model = WorkProject
    template_name = "work_project_list.html"

class WorkProjectCreateView(CreateView):
    form_class = WorkProjectForm
    template_name = 'work_project_form.html'
    success_url = reverse_lazy('work_project_list')


class WorkProjectDetailView(DetailView):
    model = WorkProject
    template_name = "work_project_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(WorkProjectDetailView, self).get_context_data(**kwargs)
        context['membership'] = Membership.objects.filter(employee=self.get_object())
        return context
    

