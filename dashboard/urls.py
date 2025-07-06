from django.urls import path
from .views import (
    admin_dashboard,
    company_dashboard,
    all_departments_dashboard,
    my_department_dashboard,
    budget_allocation,
    financial_reports,
    payslips_view,
    financial_documents,
    my_department_reports,
    company_charts_view,
    department_charts_view,
)

urlpatterns = [
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('company/', company_dashboard, name='company_dashboard'),
    path('departments/', all_departments_dashboard, name='all_departments_dashboard'),
    path('my-department/', my_department_dashboard, name='my_department_dashboard'),

    path('budget/', budget_allocation, name='budget'),
    path('reports/', financial_reports, name='reports'),
    path('my-reports/', my_department_reports, name='my_reports'),
    path('payslips/', payslips_view, name='payslips'),
    path('documents/', financial_documents, name='documents'),

    path('charts/company/', company_charts_view, name='company_charts'),
    path('charts/departments/', department_charts_view, name='department_charts'),
]
