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


def test_logout(persisted_user):
    """
    GIVEN a user already logged in
    WHEN logout is attempted
    THEN is user successfully removed from the session

    right now this test does not actually test anything other than the fact that '/logout' results in a redirect
    """

    with app.test_client() as test_client:
        
        resp = test_client.get("/logout")
        # Make sure it redirects
        assert resp.status_code == HTTPStatus.FOUND