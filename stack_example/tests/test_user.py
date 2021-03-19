import pytest
from user.serializers import UserSerializer
from user.models import User
from django.core.exceptions import ValidationError

def test_model():
    user = User(name="A" * 43)
    try:
        user.clean_fields()
    except ValidationError as e:
        assert e.message_dict['name'][0] == "I am happy to see you 42."

class TestUserSerializer():
    def test_name(self) -> None:
        data = {
            "name": "A" * 43,
            }
        serializer = UserSerializer(data=data)
        assert serializer.is_valid() is False
        assert str(serializer.errors["name"][0]) == "I am happy to see you 42."
