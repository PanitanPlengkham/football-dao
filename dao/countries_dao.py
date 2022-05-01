from sqlalchemy.orm import Session
from models.countries import Countries


class CountriesDao:
    """DAO for countries model."""

    def __init__(self, session: Session):
        self.__session = session

    def get_footballer(self):
        """Show all footballer."""
        return self.__session.query(Countries).all()

    def get_countries_by_id(self, id):
        """Get countries by id."""
        try:
            return self.__session.query(Countries).filter_by(id=id).first()
        except:
            print("There is no character with id" + id)

    def add_countries(self, countries: Countries):
        """Add the countries."""
        self.__session.add(countries)
        self.__session.commit()
        print("Added countries successfully!")

    def update_countries_name(self, id, new_name):
        """Update countries name query by ID"""
        try:
            find_char = self.__session.query(Countries).filter_by(id=id).first()
            find_char.countries_name = new_name
            self.__session.commit()
            print("Update Countries name successfully!")
        except:
            print("There is no countries with id" + id)

    def delete_countries(self, id):
        """Delete countries query by ID"""
        try:
            find_countries = self.__session.query(Countries).filter_by(id=id).first()
            self.__session.delete(find_countries)
        except:
            print("There is no countries with id" + id)


