from typing import Any
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


def validate_email_address(email: str):
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError(_("Enter a valid email address!"))


class UserManager(DjangoUserManager):

    def _create_user(self, username: str, email: str, password: str, **extra_fields):
        if not username:
            raise ValueError(_("A username must be provided !"))

        if not email:
            raise ValueError(_("An email must be provided !"))

        email = self.normalize_email(email)
        validate_email_address(email)

        global_user_model = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)

        username = global_user_model.normalize_username(username)

        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username: str, email: str, password: str, **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(
        self, username: str, email: str, password: str, **extra_fields: Any
    ) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", self.model.Role.ADMIN)  

        if extra_fields.get("is_staff") is not True:
            raise ValueError("A superuser must be a STAFF!")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("A superuser must be a SUPERUSER!")

        return self.create_user(username, email, password, **extra_fields)
