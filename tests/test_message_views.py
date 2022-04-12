"""Message View tests."""

import os

from models import Message, User
from app import app, CURR_USER_KEY
from http import HTTPStatus


def test_add_message(persisted_user):
    """Can use add a message?"""

    # Since we need to change the session to mimic logging in,
    # we need to use the changing-session trick:

    with app.test_client() as test_client:
        with test_client.session_transaction() as test_session:
            test_session[CURR_USER_KEY] = persisted_user.id

        # Now, that session setting is saved, so we can have
        # the rest of ours test

        resp = test_client.post("/messages/new", data={"text": "Hello"})

        # Make sure it redirects
        assert resp.status_code == HTTPStatus.FOUND

        msg = Message.query.one()
        assert msg.text == "Hello"
