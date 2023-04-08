from base.models import BaseUser
from django.db import models
from .validators import validate_age

CLASS_CHOICES = (("8th","8th"),("9th","9th"),("10th","10th"),("11th","11th"),("12th","12th"))


class CustomerModel(BaseUser):
    points = models.IntegerField(default=0)
    age = models.IntegerField(default=18, validators=[validate_age])
    token = models.CharField(max_length=50, null=True, blank=True)
    standerd = models.CharField(choices=CLASS_CHOICES, max_length=50, default=CLASS_CHOICES[0])
    def __str__(self):
        return self.email
    class Meta:
        db_table = 'customer'

