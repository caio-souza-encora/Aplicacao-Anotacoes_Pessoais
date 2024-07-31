from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, UUID, String, DateTime
from datetime import datetime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
