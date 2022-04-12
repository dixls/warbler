from cgi import test
import pytest
from models import Message, User, Follows
from models import db, connect_db
from app import app


@pytest.fixture
def test_app():
    app.config.from_object("config.TestingConfig")
    return app


@pytest.fixture
def test_db(test_app):
    connect_db(test_app)
    db.create_all()
    yield db
    db.session.close()
    db.drop_all()


@pytest.fixture()
def test_user():
    user = User(email="test@test.user", username="test_user", password="testpassword")
    return user


@pytest.fixture()
def test_user2():
    user = User(email="test2@user.test", username="test_user2", password="testpassword2")
    return user


@pytest.fixture()
def test_user_no_password():
    user = User(email="nopass@user.test", username="nopass_user")

@pytest.fixture
def persisted_user(test_db, test_user):
    test_db.session.add(test_user)
    test_db.session.commit()
    return test_user


@pytest.fixture
def persisted_user2(test_db, test_user2):
    test_db.session.add(test_user2)
    test_db.session.commit()
    return test_user2


@pytest.fixture()
def new_message():
    message = Message()