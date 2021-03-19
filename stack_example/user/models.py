from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,
        PermissionsMixin,
        )

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField("Name", max_length=42, null=True, 
        error_messages={'max_length':"I am happy to see you %(limit_value)s."})
