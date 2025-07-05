from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

@login_required
def role_based_dashboard_redirect(request):
    user = request.user

    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'company_accountant':
        return redirect('company_dashboard')
    elif user.role == 'department_accountant':
        return redirect('all_departments_dashboard')
    elif user.role == 'department_manager':
        return redirect('my_department_dashboard')
    else:
        return redirect('login') # Redirect to login if role is not recognized

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin.html')

@login_required
def company_dashboard(request):
    return render(request, 'dashboard/company.html')

@login_required
def all_departments_dashboard(request):
    return render(request, 'dashboard/departments.html')

@login_required
def my_department_dashboard(request):
    return render(request, 'dashboard/my_department.html')
