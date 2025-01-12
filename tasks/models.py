from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Employee
from company.models import Company


class Project(models.Model):
    assigned_employees = models.ManyToManyField(Employee, related_name="project_employees")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_tasks")
    name = models.CharField(_("Project Name"), max_length=50)
    description = models.TextField(_("Description"), max_length=1000)
    start_date = models.DateTimeField(_("Start Date"), auto_now_add=True)
    end_date = models.DateTimeField(_("End Date"), auto_now_add=True)
