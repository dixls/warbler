"""User View tests."""

import os

from models import Message, User
from app import app, CURR_USER_KEY
from http import HTTPStatus


def test_login(persisted_user):
    """
    GIVEN a valid user
    WHEN login is attempted
    THEN user is routed appropriately
    """

    with app.test_client() as test_client:
        
        resp = test_client.post("/login", data={"username": "test_user", "password": "testpassword"})

        # Make sure it redirects
        assert resp.status_code == HTTPStatus.FOUND
        # assert b"Hello, test_user!" in resp.data


# def test_login(persisted_user):
#     """
#     GIVEN a valid user
#     WHEN login is attempted
#     THEN user is routed appropriately
#     """

#     with app.test_client() as test_client:
#         with test_client.session_transaction() as test_session:
#             test_session[CURR_USER_KEY] = persisted_user.id

#         # Now, that session setting is saved, so we can have
#         # the rest of ours test

#         resp = test_client.post("/login", data={"text": "Hello"})

#         # Make sure it redirects
#         assert resp.status_code == HTTPStatus.FOUND

#         msg = Message.query.one()
#         assert msg.text == "Hello"
