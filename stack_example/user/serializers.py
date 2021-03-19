from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name"]
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False, "allow_null": False},
        }

    def validate_name(self, value):
        # I straight up raise an exception to show it doesnt even go into this validator
        max_length = self.Meta.model.name.max_length
        raise serializers.ValidationError(f"I am happy to see you {max_length}.")
