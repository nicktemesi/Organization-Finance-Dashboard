from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    FinancialReport,
    Employee,
    Payslip,
    BudgetAllocation,
    FinancialDocument,
    Department,
)
from django.contrib.auth import get_user_model
from django.db.models import Sum

User = get_user_model()

# DASHBOARDS

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin.html')

@login_required
def company_dashboard(request):
    return render(request, 'dashboard/company.html')

@login_required
def all_departments_dashboard(request):
    if request.user.role not in ['admin', 'company_accountant', 'department_accountant']:
        return redirect('login')

    departments = Department.objects.all()
    return render(request, 'dashboard/departments.html', {'departments': departments})

@login_required
def my_department_dashboard(request):
    return render(request, 'dashboard/my_department.html')


# BUDGET

@login_required
def budget_allocation(request):
    if request.user.role not in ['admin', 'company_accountant']:
        return redirect('login')

    budgets = BudgetAllocation.objects.select_related('department').all()
    return render(request, 'dashboard/budget.html', {'budgets': budgets})


# REPORTS

@login_required
def financial_reports(request):
    if request.user.role in ['admin', 'company_accountant']:
        reports = FinancialReport.objects.filter(department__isnull=True)
    elif request.user.role == 'department_accountant':
        reports = FinancialReport.objects.all()
    elif request.user.role == 'department_manager':
        if hasattr(request.user, 'employee') and request.user.employee.department:
            dept = request.user.employee.department
            reports = FinancialReport.objects.filter(department=dept)
        else:
            reports = []
    else:
        reports = []

    return render(request, 'dashboard/reports.html', {'reports': reports})


# MY REPORTS (for department manager)

@login_required
def my_department_reports(request):
    if request.user.role != 'department_manager':
        return redirect('login')

    employee = getattr(request.user, 'employee', None)
    if not employee or not employee.department:
        return render(request, 'dashboard/my_reports.html', {'reports': []})

    reports = FinancialReport.objects.filter(department=employee.department)
    return render(request, 'dashboard/my_reports.html', {'reports': reports})


# PAYSLIPS

@login_required
def payslips_view(request):
    if request.user.role not in ['admin', 'company_accountant']:
        return redirect('login')

    payslips = Payslip.objects.select_related('employee__user').all()
    return render(request, 'dashboard/payslips.html', {'payslips': payslips})


# FINANCIAL DOCUMENTS

@login_required
def financial_documents(request):
    if request.user.role != 'company_accountant':
        return redirect('login')

    documents = FinancialDocument.objects.all()
    return render(request, 'dashboard/documents.html', {'documents': documents})


# CHARTS (e.g., summary views)

@login_required
def company_charts_view(request):
    if request.user.role not in ['admin', 'company_accountant']:
        return redirect('login')

    income_total = FinancialReport.objects.filter(department__isnull=True).aggregate(Sum('total_income'))['total_income__sum'] or 0
    expenses_total = FinancialReport.objects.filter(department__isnull=True).aggregate(Sum('total_expenses'))['total_expenses__sum'] or 0

    return render(request, 'dashboard/charts/company_chart.html', {
        'income_total': income_total,
        'expenses_total': expenses_total,
    })

@login_required
def department_charts_view(request):
    if request.user.role not in ['admin', 'company_accountant']:
        return redirect('login')

    departments = Department.objects.all()
    department_data = []

    for dept in departments:
        income = FinancialReport.objects.filter(department=dept).aggregate(Sum('total_income'))['total_income__sum'] or 0
        expenses = FinancialReport.objects.filter(department=dept).aggregate(Sum('total_expenses'))['total_expenses__sum'] or 0
        department_data.append({
            'name': dept.name,
            'income': income,
            'expenses': expenses,
        })

    return render(request, 'dashboard/charts/department_chart.html', {
        'department_data': department_data
    })

@login_required
def department_detail_view(request, dept_id):
    if request.user.role not in ['admin', 'company_accountant', 'department_accountant']:
        return redirect('dashboard_redirect')

    department = get_object_or_404(Department, id=dept_id)
    staff = Employee.objects.filter(department=department)
    reports = FinancialReport.objects.filter(department=department)
    budget = BudgetAllocation.objects.filter(department=department).first()

    return render(request, 'dashboard/departments/detail.html', {
        'department': department,
        'staff': staff,
        'reports': reports,
        'budget': budget,
    })
