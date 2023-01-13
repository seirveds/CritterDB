from calendar import month_name
from collections import defaultdict
from datetime import datetime
from typing import Union
from src.scraper.database import CritterDatabase
from src.scraper.utils import db_path

db = CritterDatabase(db_path)

games = [
    "animalcrossing",
    "wildworld",
    "cityfolk",
    "newleaf",
    "newhorizons",
]

available_now_query = """
    SELECT *
    FROM CRITTERS
    WHERE id IN (
        SELECT DISTINCT 
            C.id
        FROM CRITTERS AS C,
            json_each(months_available) AS MONTHS,
            json_each(time_available, '$.{m}') AS TIME
        WHERE MONTHS.value like {m}
        AND TIME.value like {h}
        AND LOWER(REPLACE(C.game, ' ', '')) == '{game}'
    )
"""

monthly_critters_query = """
    SELECT *
    FROM CRITTERS
    WHERE id IN (
        SELECT DISTINCT 
            C.id
        FROM CRITTERS AS C,
            json_each(months_available) AS MONTHS
        WHERE MONTHS.value like {m}
        AND LOWER(REPLACE(C.game, ' ', '')) == '{game}'
    )
"""

all_query = "SELECT * FROM CRITTERS WHERE LOWER(REPLACE(game, ' ', '')) == '{game}'"

def get_month_and_hour() -> Union[int, int]:
    """Return month number and hour (24h clock)."""
    now = datetime.now()
    return now.month, now.hour

def group_query_result(res: list[dict]) -> dict:
    """Group list of dictionaries by type"""
    grouped = defaultdict(list)

    for row in res:
        grouped[row["type"]].append(row)

    return grouped

def get_all_critters(game: str) -> dict:
    """Return all critters for passed game grouped by type."""
    return group_query_result(db.query(all_query.format(game=game)))

def get_available_critters(game: str) -> dict:
    """Return critters available now in passed game grouped by type."""
    m, h = get_month_and_hour()
    res = db.query(available_now_query.format(m=m, h=h, game=game))
    return group_query_result(res)

def get_monthly_critters(game: str, month: str) -> dict:
    """Return critters available for passed month in passed game grouped by type."""
    month_index = [m for m in month_name].index(month)
    print(month_index)
    res = db.query(monthly_critters_query.format(m=month_index, game=game))
    return group_query_result(res)
