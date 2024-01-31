from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import relationship

from src.app.models.domains.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    files = relationship("File")
