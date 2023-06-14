import uuid
from sqlalchemy import Column, Integer, String, UUID

from flask_app.db.models import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    access_token = Column(String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username