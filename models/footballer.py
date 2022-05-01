from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Footballer(Base):
    __tablename__ = "footballer"
    id = Column(Integer, primary_key=True)
    footballer_name = Column(Text(30))
    goals_score = Column(Integer)
    countries = Column(Text)
    weak_foot = Column(Text)

    def __repr__(self):
        return f"Footballer(id={self.id}, footballer_name={self.footballer_name}, goals_score={self.goals_score},countries={self.countries},weak_foot{self.weak_foot})"
