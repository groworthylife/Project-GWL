from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def validate_age(a):
    if a<10 or a>100:
        raise ValidationError("Age cannot take this value", code=404)
    else:
        return a

