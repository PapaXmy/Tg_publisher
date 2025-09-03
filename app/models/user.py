from sqlalchemy import Boolean, Column, Integer, String

from app.models.base import Base


class User(Base):
    __table__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
