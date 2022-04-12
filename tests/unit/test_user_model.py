"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py

from app import app
from models import db, connect_db


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
