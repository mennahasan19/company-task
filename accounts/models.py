from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = 'Manager', 'Manager'
        EMPLOYEE = "EMPLOYEE", "Employee"

    username = models.CharField(_("Username"), max_length=50, unique=True)
    email = models.EmailField(_("Email"), max_length=100, unique=True)

    role = models.CharField(_("Role"), choices=Role.choices, blank=True, null=True)

    manager = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_profile")
    name = models.CharField(_("Name"), max_length=50)
    phone = models.PhoneNumberField(_("Phone Number"))
    address = models.CharField(_("Address"), max_length=150)
    designation = models.CharField(max_length=100)
    hired_on = models.DateTimeField(_("Hired on"), auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    assigned_employees = models.ManyToManyField('Employee', related_name="projects")
    name = models.CharField(_("Project Name"), max_length=50)
    description = models.TextField(_("Description"), max_length=1000)
    start_date = models.DateTimeField(_("Start Date"), auto_now_add=True)
    end_date = models.DateTimeField(_("End Date"), auto_now_add=True)


class Company(models.Model):
    name = models.CharField(_("Company Name"), max_length=50)
    department_num = models.PositiveIntegerField(_("Number of Departments"))
    employee_num = models.PositiveIntegerField(_("Number of Employees"))
    project_num = models.PositiveIntegerField(_("Number of Projects"))
    
    
class Department(models.Model):
    company = models.ForeignKey("company", on_delete=models.CASCADE, related_name="company_department")
    name = models.CharField(_("Department Name"), max_length=50)