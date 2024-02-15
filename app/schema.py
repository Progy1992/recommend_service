from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime


class Book(Base):
    __tablename__ = "book"

    isbn = Column(String(255), primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    publicationYear = Column(Integer, nullable=False)
    publisher = Column(String(255), nullable=False)
    image = Column(String(500))
    id = Column(Integer, unique=True, autoincrement=True)
    is_active = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False, onupdate=datetime.utcnow())
