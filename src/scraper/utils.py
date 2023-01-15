from base64 import b64encode
from calendar import month_abbr
from datetime import datetime
import re
from bs4.element import Tag
from bs4 import BeautifulSoup as bs
import requests

db_path = "data/critters.db"

base_url = "https://nookipedia.com"

url_blacklist = [
    "https://nookipedia.com/wiki/Herabuna",  # e+ exclusive
    "https://nookipedia.com/wiki/Moon_jellyfish",  # Available for half a month, dive critter in NH, fish in other games
    # "https://nookipedia.com/wiki/Horned_elephant",  # TEMP
    # "https://nookipedia.com/wiki/Stinkbug",  # TEMP
    # "https://nookipedia.com/wiki/Eel",  # TEMP
    # "https://nookipedia.com/wiki/Rainbow_trout",  # TEMP
    # "https://nookipedia.com/wiki/Octopus_(fish)",  # TEMP
]


def get_critter_list_from_url(url: str) -> list[str]:
    """Return urls to all critters listed on Fish, Bug, or Sea creature overview page."""
    soup = url_to_soup(url)
    # Find correct table using class name
    table = soup.find("table", class_="styled")
    # Parse table to get all critter names and links to their wiki page
    # Start at index 3 to remove headers
    rows = table.find_all("tr")[3:]
    # First td element is the one we want, so use .find
    a_tags = [row.find("td").find("a") for row in rows]
    return [f"{base_url}{a['href']}" for a in a_tags]


def url_to_soup(url: str) -> bs:
    """Make get request to passed url and return html parsed to soup."""
    html = requests.get(url).text
    soup = bs(html, features="html.parser")
    return soup


def get_infobox_type(infobox: Tag) -> str:
    """Return type of inbobox (fish, bug, sea creature) based on background color of div."""
    bg_color = re.search(r"background: (#[0-9a-f]{6})", infobox["style"].lower()).group(1)
    if bg_color == "#caed78":
        return "bug"
    elif bg_color == "#66ccff":
        return "fish"
    elif bg_color == "#66a6ff":
        return "sea_creature"
    else:
        raise Exception(f"Unexpected background color {bg_color}")


def image_url_to_b64(url: str) -> str:
    """GETs an image from passed url and returns as base64 encoded string."""
    return b64encode(requests.get(url).content).decode('utf-8')


def month_abbr_to_num(abbr: str) -> int:
    """Turns month abbreviation (e.g. Dec) to month number (12)."""
    return list(month_abbr).index(abbr)


def am_pm_to_universal_time(time: str) -> int:
    """Turn time string like 8 PM to universal hour (20)"""
    return int(datetime.strptime(time, "%I %p").strftime("%H"))


def month_range_to_month_numbers(month_range: str) -> list[int]:
    """
    Turns month range string like (Jun - Aug) or Jun - Aug to list with month numbers in
    range ([6, 7, 8]). Also works for single months like (Jun) or Jun.
    """
    # Remove parentheses from month_range string
    month_range = re.sub(r"[\(\)]", "", month_range)

    # Normalize dashes, en-dashes are used more so we replace normal dashes
    month_range = month_range.replace("-", "–")
    
    # Handles month range like (Jun - Aug)
    if "–" in month_range:
        from_month, to_month = month_range.split("–")
        from_month = month_abbr_to_num(from_month.strip()[:3])
        to_month = month_abbr_to_num(to_month.strip()[:3])
        if from_month < to_month:
            month_range = [m for m in range(from_month, to_month + 1)]
        else:
            month_range = [m for m in range(1, to_month + 1)] + [m for m in range(from_month, 13)]
    # Handles single months like (Jun)
    else:
        month_range = [month_abbr_to_num(month_range.strip()[:3])]
    assert len(month_range) > 0
    return month_range


def hour_range_to_hour_numbers(hour_range: str) -> list[int]:
    """
    Turns hour range string like (8 AM - 1 PM) to list with hour numbers in
    range ([8, 9, 10, 11, 12, 13]). Also works for single hours like (8 AM).
    Parentheses in input string are optional.
    """
    # Remove parentheses
    hour_range = re.sub(r"[\(\)]", "", hour_range)

    # Normalize dashes, en-dashes are used more so we replace normal dashes
    hour_range = hour_range.replace("-", "–")

    if "–" in hour_range:
        from_hour, to_hour = hour_range.split("–")
        from_hour = am_pm_to_universal_time(from_hour.strip())
        to_hour = am_pm_to_universal_time(to_hour.strip())
        if from_hour < to_hour:
            hour_range = [h for h in range(from_hour, to_hour + 1)]
        else:
            hour_range = [h for h in range(0, to_hour + 1)] + [h for h in range(from_hour, 24)]
    else:
        hour_range = [am_pm_to_universal_time(hour_range.strip())]
    assert len(hour_range) > 0
    return hour_range
