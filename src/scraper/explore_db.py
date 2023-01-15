from src.scraper.database import CritterDatabase
from src.scraper.utils import db_path

db = CritterDatabase(db_path)

for row in db.query("SELECT name, game, time_available FROM CRITTERS WHERE NAME == 'Vampire squid'"):
    print(row)
