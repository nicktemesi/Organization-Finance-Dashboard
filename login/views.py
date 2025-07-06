from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard_redirect')

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

