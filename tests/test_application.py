import pytest
from application import authorized, application
from models import Email, db


@pytest.fixture
def client():
    db.create_all()
    return application.test_client()


class TestApplication:

    def test_authorized(self):
        red_sesion = '123'
        green_sesion = '12345678'
        assert authorized(red_sesion) is False
        assert authorized(green_sesion) is True

    def test_insert_email(self, client):
        test_data = {'email': 'test@test.com', 'blocked_reason': 'test'}
        response = client.post(f'/blacklists/', json=test_data, headers={"Authorization": "123456789"})
        assert response.status_code == 200
        db.session.query(Email).filter(Email.email == test_data['email']).delete()
        db.session.commit()

    def test_find_email(self, client):
        test_email = Email(email='test_find_email@test.com', blocked_reason='test')
        db.session.query(Email).filter(Email.email == test_email.email).delete()  # Dispose
        db.session.add(test_email)
        db.session.commit()
        response = client.get(f'/blacklists/{test_email.email}', headers={"Authorization": "123456789"})
        assert response.status_code == 200

    def test_main(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"DevOps" in response.data

    def test_new_email_model(self):
        user = Email(email='patkennedy79@gmail.com')
        assert user.email == 'patkennedy79@gmail.com'
