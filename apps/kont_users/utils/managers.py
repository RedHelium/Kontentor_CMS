from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.forms import ValidationError


class KontentorUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        try:
            validate_email(email)
        except ValidationError as validation_error:
            raise validation_error

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("У суперпользователя параметр is_staff должен быть True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "У суперпользователя параметр is_superuser должен быть True."
            )

        return self.create_user(email, password, **extra_fields)
