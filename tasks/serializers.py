from rest_framework import serializers
from .models import Project
from company.serializers import CompanySerializer
from accounts.models import Employee



class SimpleEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email']

class ProjectSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    assigned_employees = SimpleEmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'company', 'assigned_employees']
