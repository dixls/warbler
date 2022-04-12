"""User model tests."""

from app import app
from models import User, Message

app.config.from_object("config.TestingConfig")

