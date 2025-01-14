from django.urls import path
from .views import (
    RegisterEmployeeView,
    RegisterManagerView,
    Login,
    user_info,
    update_user,
    delete_employee,
    update_employee_status
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register_emp/", RegisterEmployeeView.as_view(), name="register-employee"),
    path("register_manager/", RegisterManagerView.as_view(), name="register-manager"),
    path("login/", Login.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("user_info/", user_info, name="user-information"),
    path("update/", update_user, name="user-update"),
    path("delete/<int:employee_id>/", delete_employee, name="delete-employee"),
    path("update/employee_status/<int:employee_id>/", update_employee_status, name="update-employee-status"),
]
