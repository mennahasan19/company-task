from django.urls import path
from .views import RegisterEmployeeView, RegisterManagerView, Login, user_info, update_user
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register_emp/", RegisterEmployeeView.as_view(), name="register-employee"),
    path("register_manager/", RegisterManagerView.as_view(), name="register-manager"),
    path("login/", Login.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("user_info/", user_info, name="user-information"),
    path("update/", update_user, name="user-update"),
]
