from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'doctor'),
        (2, 'pharmacy'),
        (3, 'patient')
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)