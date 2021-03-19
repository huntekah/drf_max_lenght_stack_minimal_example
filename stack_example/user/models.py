from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import MaxLengthValidator

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        "Name",
        max_length=42,
        null=True,
        validators=[MaxLengthValidator(42, "I am happy to see you {max_length}.")],
    )
