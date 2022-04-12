"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py

from distutils.log import error
from app import app
from models import db, connect_db, User


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

app.config.from_object("config.TestingConfig")


def test_user_model(test_db, test_user):
    """Does basic model work?"""
    
    test_db.session.add(test_user)
    test_db.session.commit()

    # User should have no messages & no followers
    assert len(test_user.messages) == 0
    assert len(test_user.followers) == 0


def test_is_following(test_db, test_user, test_user2):
    """
    GIVEN 2 users
    WHEN 1 user follows another
    THEN does the is_following class function reflect that?
    """
    test_db.session.add(test_user2)
    test_db.session.add(test_user)
    test_user.followers.append(test_user2)
    test_db.session.commit()

    assert test_user2.is_following(test_user)
    assert test_user.is_followed_by(test_user2)


def test_is_not_following(test_db, test_user, test_user2):
    """
    GIVEN 2 users
    WHEN 1 user follows another
    THEN does the is_following class function reflect that?
    """
    test_db.session.add(test_user2)
    test_db.session.add(test_user)
    test_db.session.commit()

    assert test_user2.is_following(test_user) == False
    assert test_user.is_followed_by(test_user2) == False


def test_user_signup(test_db):
    """
    GIVEN appropriate user credentials
    WHEN calling the user.signup method
    THEN does the user get successfully signed up?
    """

    signup_user = User.signup("signup_user", "signup@test.user", "signup_password")
    test_db.session.commit()

    assert signup_user.id
    assert signup_user.image_url == "/static/images/default-pic.png"


def test_user_signup_nopass(test_db):
    """
    GIVEN appropriate user credentials
    WHEN calling the user.signup method
    THEN does the user get successfully signed up?
    """

    try:
        signup_user = User.signup("signup_user", "signup@test.user")
        test_db.session.commit()
        assert False
    except:
        assert True


def test_user_authenticate(persisted_user):
    """
    GIVEN a user that exists
    WHEN appropriate credentials are used to login
    THEN authentication will succeed
    """

    login = User.authenticate("test_user", "testpassword")

    assert login.username == "test_user"
    assert login.id


def test_user_authenticate_wrong_username(persisted_user):
    """
    GIVEN a user that exists
    WHEN invalid username is given
    THEN authentication will fail
    """
    try:
        login = User.authenticate("test_usser", "testpassword")
        assert False
    except:
        assert True


def test_user_authenticate_wrong_password(persisted_user):
    """
    GIVEN a user that exists
    WHEN invalid password is given
    THEN authentication will fail
    """
    try:
        login = User.authenticate("test_user", "testpasssword")
        assert False
    except:
        assert True