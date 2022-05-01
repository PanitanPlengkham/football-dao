from footballer_star import Footballer

footballer_db = Footballer.get_instance()


footballer_dao = footballer_db.get_character_dao()
countries_dao = footballer_db.get_weapon_dao()
