import pytest
from user.serializers import UserSerializer

class TestUserSerializer():
    def test_name(self) -> None:
        data = {
            "name": "A" * 43,
            }
        serializer = UserSerializer(data=data)
        assert serializer.is_valid() is False
        assert str(serializer.errors["name"][0]) == "I am happy to see you 42."
