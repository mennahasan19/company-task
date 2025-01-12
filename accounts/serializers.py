import datetime
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import User,Employee


class LoginSerializer(TokenObtainPairSerializer):
    """
    Custom token serializer to include additional user data in the token.
    """

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Check if the email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("This email is not registered.")

        # Authenticate the user
        if not authenticate(email=email, password=password):
            raise serializers.ValidationError("Incorrect password.")

        # Get the standard token data
        data = super().validate(attrs)
        # Add custom user data to the response
        user_info = {
            "username": user.username,
            "email": user.email,
            "role": user.role,
        }
        data.update(user_info)
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims to the token
        token["username"] = user.username
        token["email"] = user.email
        token["role"] = user.role

        return token


class RegisterSerializer(serializers.ModelSerializer):
    """
    Base serializer for user registration.
    """

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    def validate_email(self, value):
        # Ensure email is unique
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already registered.")
        return value

    def validate(self, attrs):
        # Ensure passwords match
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create_user(self, validated_data, role):
        # Remove confirm_password from validated data
        validated_data.pop("confirm_password")
        # Create the user
        user = User.objects.create_user(**validated_data)
        # Assign role to the user
        user.role = role
        user.save()
        return user


class RegisterEmployeeSerializer(RegisterSerializer):
    """
    Serializer for employee registration.
    """

    role = serializers.CharField(read_only=True, default=User.Role.EMPLOYEE)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "role",
        ]

    def create(self, validated_data):

        return self.create_user(validated_data, User.Role.EMPLOYEE)


class RegisterManagerSerializer(RegisterSerializer):
    """
    Serializer for manager registration.
    """

    role = serializers.CharField(read_only=True, default=User.Role.MANAGER)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "role",
        ]

    def create(self, validated_data):
        return self.create_user(validated_data, User.Role.MANAGER)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    role = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "role",
        )


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    days_employed = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = ["id", "name", "address", "phone", "hired_on",
                "designation", "days_employed", "user", "workflow"]
        
        
    def get_days_employed(self, obj):
        return (datetime.now() - obj.hired_on).days