from typing import Dict

from sqlalchemy import (
    Column, BigInteger, String,
    ForeignKey, DateTime, Integer
)
from sqlalchemy.sql import func

from src.app.models.domains.user import Base


class FileModel(Base):
    __tablename__ = "file_info"

    id = Column(BigInteger, primary_key=True)
    filename = Column(String)
    conversion_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    user_id = Column(Integer, ForeignKey("users.id", ondelete="NO ACTION"))

    def model_dump(self) -> Dict:
        return {
            "id": self.id,
            "filename": self.filename,
            "conversion_date": self.conversion_date.isoformat(),
            "user_id": self.user_id
        }
