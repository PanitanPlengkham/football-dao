from sqlalchemy.orm import Session
from models.footballer import Footballer


class FootballerDao:
    """DAO for footballer model."""

    def __init__(self, session: Session):
        self.__session = session

    def get_footballer(self):
        """Show all footballer."""
        return self.__session.query(Footballer).all()

    def get_weapon_by_id(self, id):
        """Get footballer by id."""
        try:
            return self.__session.query(Footballer).filter_by(id=id).first()
        except:
            print("There is no footballer with id" + id)

    def add_footballer(self, footballer: Footballer):
        """Add the footballer."""
        self.__session.add(footballer)
        self.__session.commit()
        print("Added footballer successfully!")

    def update_footballer_name(self, id, new_name):
        """Update footballer name query by ID"""
        try:
            find_footballer = self.__session.query(Footballer).filter_by(id=id).first()
            find_footballer.footballer_name = new_name
            self.__session.commit()
            print("Update footballer name successfully!")
        except:
            print("There is no footballer with id" + id)

    def delete_footballer(self, id):
        """Delete footballer query by ID"""
        try:
            find_footballer = self.__session.query(Footballer).filter_by(id=id).first()
            self.__session.delete(find_footballer)
        except:
            print("There is no footballer with id" + id)


