from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.countries_dao import CountriesDao
from dao.footballer_dao import FootballerDao


class Footballer:
    countries_dao = None
    footballer_dao = None
    __instance = None

    @staticmethod
    def get_instance():
        """Static method access"""
        if Footballer.__instance is None:
            Footballer.__instance = Footballer()
        return Footballer.__instance

    def __init__(self, connection_url="sqlite:///footballer-data.db"):
        engine = create_engine(connection_url, echo=True)
        Session = sessionmaker(bind=engine)
        self.__db_session = Session()

    def get_footballer_dao(self):
        """Get footballer dao."""
        if self.footballer_dao is None:
            self.footballer_dao = FootballerDao(session=self.__db_session)
        return self.footballer_dao

    def get_countries_dao(self):
        """Get countries dao."""
        if self.countries_dao is None:
            self.countries_dao = CountriesDao(session=self.__db_session)
        return self.countries_dao

    def close_db(self):
        """Close all the database"""
        self.__db_session.close()