from src.scraper.database import CritterDatabase
from src.scraper.utils import db_path

db = CritterDatabase(db_path)

for row in db.query("SELECT * FROM CRITTERS WHERE Name == 'Lobster' order by game"):
    del row["b64_img"]
    del row["months_available"]
    del row["time_available"]
    print(row)
