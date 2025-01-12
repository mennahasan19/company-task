from .serializers import (
    LoginSerializer,
    RegisterManagerSerializer,
    RegisterEmployeeSerializer,
    UserSerializer,
)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        # Replace `is_Manager` with your actual condition
        return request.user and request.user.is_authenticated and request.user.role == "MANAGER"


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        # Replace `is_Employee` with your actual condition
        return request.user and request.user.is_authenticated and request.user.role == "EMPLOYEE"


# Custom token obtain pair view
class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


# Register Employee view
class RegisterEmployeeView(generics.CreateAPIView):
    queryset = User.objects.filter(role=User.Role.EMPLOYEE)
    permission_classes = [AllowAny]
    serializer_class = RegisterEmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(role=User.Role.EMPLOYEE)


# Register Manager view
class RegisterManagerView(generics.CreateAPIView):
    queryset = User.objects.filter(role=User.Role.MANAGER)
    permission_classes = [AllowAny]
    serializer_class = RegisterManagerSerializer

    def perform_create(self, serializer):
        serializer.save(role=User.Role.MANAGER)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    if user.role == "MANAGER":
        manager = request.user
        serializer = UserSerializer(manager)
    elif user.role == "EMPLOYEE":
        employee = request.user
        serializer = UserSerializer(employee)
    else:
        return Response({"Message": f"You are admin {user.username}"}, status=status.HTTP_200_OK)
    return Response({"data": serializer.data})


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request):
    data = request.data
    user = request.user
    if "password" in data:
        if "password" == "confirm_password":
            user.password = make_password(data["password"])
            user.save()
        return Response({"message:": "password do not match"})
    serializer = UserSerializer(instance=user, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
