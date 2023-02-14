from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True)
    sample_id = Column(String)
