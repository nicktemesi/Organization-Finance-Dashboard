from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FinancialReport(models.Model):
    REPORT_TYPES = (
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annual', 'Annual'),
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    report_date = models.DateField()
    total_income = models.DecimalField(max_digits=12, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2)
    summary = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def is_company_report(self):
        return self.department is None

    def net_income(self):
        return self.total_income - self.total_expenses

    def __str__(self):
        return f"{self.report_type.title()} Report - {self.report_date}"

class Employee(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bank_account = models.CharField(max_length=100)
    is_salary_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.user.username} - {self.month.strftime('%B %Y')}"

class BudgetAllocation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    allocated_date = models.DateField(auto_now_add=True)
    allocated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.department.name} - {self.amount}"

class FinancialDocument(models.Model):
    DOC_TYPES = (
        ('balance_sheet', 'Balance Sheet'),
        ('profit_loss', 'Profit and Loss Statement'),
        ('cash_flow', 'Cash Flow Statement'),
        ('tax_return', 'Tax Return'),
    )

    doc_type = models.CharField(max_length=50, choices=DOC_TYPES)
    report_period = models.CharField(max_length=100)  # e.g. 'Q2 2025'
    content = models.TextField()  # or FileField if uploading PDFs
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_doc_type_display()} - {self.report_period}"
