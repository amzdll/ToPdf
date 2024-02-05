from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import relationship

from src.app.models.domains.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    files = relationship("FileModel")
