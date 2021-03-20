from rest_framework import serializers
from user.models import User
from rest_framework import fields
from django.utils.translation import gettext_lazy as _


class CustomCharField(fields.CharField):
    default_error_messages = {
        "max_length": _("I am happy to see you {max_length}."),
    }


class UserSerializer(serializers.ModelSerializer):
    name = CustomCharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        max_length=42,
    )

    class Meta:
        model = User
        fields = ["name"]
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False, "allow_null": False},
        }
