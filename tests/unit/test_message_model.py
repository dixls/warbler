"""User model tests."""

from hashlib import new
from app import app
from models import User, Message, Likes

app.config.from_object("config.TestingConfig")

def test_message_model(test_db, new_message):
    """
    GIVEN appropriate message parameters
    WHEN creating a message is attempted
    THEN is the message successfully created?
    """

    test_db.session.add(new_message)
    test_db.session.commit()

    assert new_message.user.username == "test_user"
    assert new_message.id
    assert new_message.timestamp


def test_message_likes(test_db, persisted_user2, persisted_message):
    """
    GIVEN a message and a user who did not create that message
    WHEN a message is added to a user's likes
    THEN does that relationship work right?
    """

    persisted_user2.likes.append(persisted_message)
    test_db.session.commit()

    assert Likes.query.get(1).message_id == 1