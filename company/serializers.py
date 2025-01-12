from rest_framework import serializers
from .models import Company, Department


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "department_num", "employee_num", "project_num"]
        
        
class DepartmentSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="company.name", read_only=True)
    class Meta:
        model = Department
        field = ["id", "name", "company"]