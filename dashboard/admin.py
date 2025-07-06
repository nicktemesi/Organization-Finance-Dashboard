from django.contrib import admin
from .models import (
    Department,
    FinancialReport,
    Employee,
    Payslip,
    BudgetAllocation,
    FinancialDocument
)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ['report_type', 'report_date', 'created_by']
    list_filter = ['report_type', 'report_date']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'role', 'salary', 'is_salary_approved', 'is_paid']
    list_filter = ['department', 'is_paid', 'is_salary_approved']

@admin.register(Payslip)
class PayslipAdmin(admin.ModelAdmin):
    list_display = ['employee', 'month', 'gross_salary', 'approved', 'paid']
    list_filter = ['approved', 'paid', 'month']

@admin.register(BudgetAllocation)
class BudgetAllocationAdmin(admin.ModelAdmin):
    list_display = ['department', 'amount', 'allocated_date', 'allocated_by']
    list_filter = ['department', 'allocated_date']

@admin.register(FinancialDocument)
class FinancialDocumentAdmin(admin.ModelAdmin):
    list_display = ['doc_type', 'report_period', 'created_at', 'created_by']
    list_filter = ['doc_type', 'created_at']
