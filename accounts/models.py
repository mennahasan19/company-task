from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from company.models import Company


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = 'MANAGER', 'Manager'
        EMPLOYEE = "EMPLOYEE", "Employee"

    username = models.CharField(_("Username"), max_length=50, unique=True)
    email = models.EmailField(_("Email"), max_length=100, unique=True)

    role = models.CharField(_("Role"), choices=Role.choices, blank=True, null=True, max_length=200)

    manager = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username



class Employee(models.Model):
    class Workflow(models.TextChoices):
        Pending_Review = "PENDING_REVIEW","Pending_Review"
        Review_Scheduled = "REVIEW_SCHEDULED","Review_Scheduled"
        Feedback_Provided = "FEEDBACK_PROVIDED","Feedback_Provided"
        Under_Approval = "UNDER_APPROVAL","Under_Approval"
        Review_Approved = "REVIEW_APPROVED","Review_Approved"
        Review_Rejected = "REVIEW_REJECTED","Review_Rejected"
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_profile")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_employee")
    name = models.CharField(_("Name"), max_length=50, blank=True, null=True)
    phone = models.CharField(_("Phone Number"), max_length=13, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    hired_on = models.DateTimeField(_("Hired on"), auto_now_add=True, blank=True, null=True)
    workflow = models.CharField(_("Workflow"), choices=Workflow.choices, blank=True, null=True, max_length=200)
    
    def __str__(self):
        return self.name
    
    

@receiver(post_save, sender=User)
def create_employee_profile(sender, created, instance, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    else:
        print("profile is already created")
    

