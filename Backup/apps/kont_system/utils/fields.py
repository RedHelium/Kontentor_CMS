from typing import Any
from django.db import models
from django.core.validators import RegexValidator


class KontentorGenderField(models.CharField):
    """
    Полоролевая самоидентификация человека
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:

        GENDER_TYPES = [(0, "Не указано"), (1, "Мужской"), (2, "Женский")]

        kwargs["max_length"] = 10
        super().__init__(*args, **kwargs)

        self.choices = GENDER_TYPES

    @property
    def short_name(self):
        return self.name[0]

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs


class KontentorPhoneField(models.CharField):
    """
    Номер телефона
    """

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 20
        super().__init__(*args, **kwargs)

    default_validators = [
        RegexValidator(
            regex=r"^\+?\d{1,3}\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$",
            message="Номер телефона введён некорректно.",
            code="invalid_phone_number",
        )
    ]

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
