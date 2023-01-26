from calendar import month_name
from collections import defaultdict
from datetime import datetime
from typing import Union
from database import CritterDatabase

db = CritterDatabase("data/critters.db")

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


def shift_month(m: int) -> int:
    """Shift month number from northern to southern hemisphere value."""
    if m == 6:
        return 12
    return (m + 6) % 12

def shift_month_availabilities(res: list[dict]) -> list[dict]:
    """ Update query result month availability to southern hemisphere"""
    # Doesn't scale very nicely :/
    for row in res:
        row["months_available"] = [shift_month(m) for m in row["months_available"]]
    return res


def select_time_availability(res: list[dict], m: Union[int, None] = None) -> list[dict]:
    """
    Select available time for passed month from time_available entry.
    Useurrent month if no month passed. We check if this month is present
    in time_available dict, if this is not the case, we pick a random month from
    the dict to return.
    """
    if m is None:
        m, _ = get_month_and_hour()

    for row in res:
        # Check if selected month present in dict, if not, use first present key
        if str(m) not in row["time_available"]:
            m = list(row["time_available"].keys())[0]
        # Transform dict with time availabilities per month to single
        # list containing available hours for selected month
        row["time_available"] = row["time_available"][str(m)]
    return res


def get_all_critters(game: str, hemisphere: str) -> dict:
    """Return all critters for passed game grouped by type."""
    res = db.query(all_query.format(game=game))
    # Get time_available for current month if possible, otherwise
    # get time from a random month
    res = select_time_availability(res)
    if game == "newhorizons" and hemisphere == "s":
        res = shift_month_availabilities(res)
    return group_query_result(res)


def get_filtered_critters(game: str, month: str, hemisphere: str) -> dict:
    """Return critters available for passed month and hour in passed game grouped by type."""
    southern_hemisphere = (game == "newhorizons") and (hemisphere == "s")
    # If passed month is 'now' use current month
    if month == 'now':
        m, h = get_month_and_hour()
    # If passed month is actually a month transform month name into month number
    else:
        m = [mth.lower() for mth in month_name].index(month)
        h = "'%'"  # Dont look at time

    # Shift 6 months for southern hemisphere
    if southern_hemisphere:
        m = shift_month(m)

    res = db.query(available_now_query.format(m=m, h=h, game=game))
    # Month chosen for time availability is passed month
    res = select_time_availability(res, m)

    if southern_hemisphere:
        res = shift_month_availabilities(res)
    return group_query_result(res)
