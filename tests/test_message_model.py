from models import Message
import pytest
from models import db, connect_db
from app import app

app.config.from_object("config.TestingConfig")

connect_db(app)
db.create_all()

