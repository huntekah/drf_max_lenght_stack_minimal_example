from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

# Create your models here.
from rest_framework import fields


class CharField(fields.CharField):

    default_error_messages = {"max_length": "I am happy to see you {max_length}."}


class User(AbstractBaseUser, PermissionsMixin):
    name = CharField("Name", max_length=42, null=True)
