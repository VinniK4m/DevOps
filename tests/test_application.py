import pytest
from application import authorized
from application import application
from models import Email
import tempfile
import os


@pytest.fixture
def client():
    return application.test_client()


class TestApplication:

    def test_authorized(self):
        red_sesion = '123'
        green_sesion = '123456789'
        assert authorized(red_sesion) is False
        assert authorized(green_sesion) is True

    @pytest.mark.skip()
    def test_insert_email(self):
        # Todo: Implement
        pass

    @pytest.mark.skip()
    def test_find_email(self):
        # Todo: Implement
        pass

    def test_main(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"DevOps" in response.data

    def test_new_email_model(self):
        """
        GIVEN a Email model
        WHEN a new User is created
        THEN check the email
        """
        user = Email(email='patkennedy79@gmail.com')
        assert user.email == 'patkennedy79@gmail.com'
