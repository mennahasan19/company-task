from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Company(models.Model):
    name = models.CharField(_("Company Name"), max_length=50)

    @property
    def department_num(self):
        return self.company_department.count()

    @property
    def employee_num(self):
        return self.company_employee.count()

    @property
    def project_num(self):
        return self.company_project.count()
        
    def __str__(self):
        return self.name
    
    
class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_department")
    name = models.CharField(_("Department Name"), max_length=50)
    
    def __str__(self):
        return self.name
    