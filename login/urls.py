from django.urls import path
from .views import (
    CustomLoginView,
    role_based_dashboard_redirect,
    admin_dashboard,
    company_dashboard,
    all_departments_dashboard,
    my_department_dashboard
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # ✅ keep this
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', role_based_dashboard_redirect, name='dashboard_redirect'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/company/', company_dashboard, name='company_dashboard'),
    path('dashboard/departments/', all_departments_dashboard, name='all_departments_dashboard'),
    path('dashboard/my-department/', my_department_dashboard, name='my_department_dashboard'),
]
