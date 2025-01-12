from django.urls import path
from .views import get_all_companies, get_company


urlpatterns = [
    path("all/",get_all_companies, name="get-all-companies"),
    path("<int:company_id>/",get_company, name="get-company"),
    
]
