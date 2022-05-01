from sqlalchemy import Integer, Column, Text, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Countries(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    countries = Column(Text(30), ForeignKey("footballer_dao.countries"), nullable=False)
    population = Column(Integer)

    def __repr__(self):
        return f"Countries(id={self.id}, weapons_name={self.weapons_name},weapon_type={self.weapon_type})"
