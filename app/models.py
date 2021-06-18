from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary
from .dbconfig import Base


class userData(Base):
    __tablename__ = "userData"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    best_score = Column(Integer)
    game_key = Column(LargeBinary)
    board_key = Column(LargeBinary)

    # is_active = Column(Boolean, default=True)
    # items = relationship("Item", back_populates="owner")

class globalBest(Base):
    __tablename__ = "globalBest"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    global_best = Column(Integer)