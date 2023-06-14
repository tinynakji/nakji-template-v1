import pytest
import uuid

from flask_app.conftest import TestBase
from flask_app.api.users.models import User

class TestUserEndpoints(TestBase):

    def test_get_user_by_username(self, session, client):
        user = User(
            uuid=uuid.uuid4(),
            email="test@user.com",
            username="test_user",)

        session.add(user)
        session.commit()

        response = client.get(
            '/api/v1/users',
            query_string=f"username={user.username}"
        )

        assert response.status_code == 200
        assert response.json['username'] == user.username
