from sqlalchemy import (
    Column, BigInteger, String,
    ForeignKey, DateTime, Integer
)
from sqlalchemy.sql import func

from src.app.models.domains.user import Base


class File(Base):
    __tablename__ = "file_info"

    id = Column(BigInteger, primary_key=True)
    file_name = Column(String)
    conversion_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
