from .serializers import CompanySerializer
from .models import Company
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from accounts.views import IsManager

@api_view(["GET"])
@permission_classes([IsManager])
def get_all_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)
    
    
@api_view(["GET"])
@permission_classes([IsManager])
def get_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return Response({"message:":"this company does not exist"})
    serializer = CompanySerializer(company)
    return Response(serializer.data)


    
