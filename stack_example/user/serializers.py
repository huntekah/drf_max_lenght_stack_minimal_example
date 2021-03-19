from rest_framework import serializers
from user.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name"]
        extra_kwargs = {
            "name": {"required": True, "allow_blank": False, "allow_null": False, "error_messages": User._meta.get_field('name').error_messages},
        }
