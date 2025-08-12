from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Text
from database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    linkedin_id = Column(String, unique=True, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    headline = Column(String, nullable=True)
    profile_data = Column(Text, nullable=True)  # JSON string
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

class ContentCalendar(Base):
    __tablename__ = "content_calendar"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String, default="scheduled")  # scheduled, posted
    created_at = Column(DateTime, server_default=func.now())
