from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


class NonUserContactModel(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=15 ,blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name
