from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeListView.as_view() , name='employee_list'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('work_project/', views.WorkProjectListView.as_view(), name='work_project_list'),
    path('work_project/create/', views.WorkProjectCreateView.as_view(), name = 'work_project_create'),
    path('work_project/<int:pk>/', views.WorkProjectDetailView.as_view(), name='work_project_detail'),
    #path('query', views.get_queryset, name="query"),

]
