import re
from bs4.element import Tag
from utils import hour_range_to_hour_numbers, image_url_to_b64, month_range_to_month_numbers, url_to_soup, get_infobox_type


class CritterPage:
    def __init__(self, url: str):
        self.url = url

        self.soup = url_to_soup(url)
        self.title = self.soup.find("h1", class_="firstHeading").text

        self.infoboxes = []

        # Set above two infobox variables
        self.set_infoboxes_data()

    def set_infoboxes_data(self):
        """ """
        # Get the h3 elements prefixing each infobox. Using regex to filter out museum parts,
        # these contain spans ending with a digit, so we can easily remove them from list.
        # Also remove pocket camp info
        infobox_headers = [
            elem for elem in self.soup.find_all("h3")
            if elem.find("span", class_="mw-headline")
            and not re.search(r"\d$", elem.find("span", class_="mw-headline")["id"])
            and elem.find("span", class_="mw-headline")["id"].lower().startswith("in_")
            and not "pocket" in elem.find("span", class_="mw-headline").text.lower()
            and not "e+" in elem.find("span", class_="mw-headline").text
        ]

        # Name of game is in the <i> tag inside the span with class mw-headline
        infobox_names = [
            elem.find("span", class_="mw-headline").find("i").text for elem in infobox_headers
        ]

        # Infoboxes are divs right after the relevant h3 tags, using find_next we can easily get
        # these divs as they have no class or id to retrieve them with otherwise
        infobox_divs = [
            elem.find_next("div") for elem in infobox_headers
        ]

        # Parse divs to structured data in dictionary
        for game_name, infobox in zip(infobox_names, infobox_divs):
            infobox_dict = self.parse_infobox(infobox)
            infobox_dict["game"] = game_name
            self.infoboxes.append(infobox_dict)

    def parse_infobox(self, infobox: Tag) -> dict:
        """Parse all relevant data from single game critter infobox."""
        infobox_data = dict()

        infobox_data["type"] = get_infobox_type(infobox)
        infobox_data["name"] = self.title

        # Left side of infobox is easy, only three elements relevant
        infobox_data["num"] = infobox.find("small").text.replace("#", "")

        img_url = infobox.find("a", class_="image").find("img")["src"]
        infobox_data["b64_img"] = image_url_to_b64(img_url)

        infobox_data["catching_quote"] = infobox.find("i").text

        # Right side in table format and differs per game, harder to parse
        table_body = infobox.find("tbody")
        row_names = [th.text.strip() for th in table_body.find_all("th")]
        row_values = [td.text.strip() for td in table_body.find_all("td")]

        for name, value in zip(row_names, row_values):
            if name == "Time of year":
                # Keep track of available month numbers as timeframes can be disjoint
                infobox_data["months_available"] = []

                # Some times have footnotes, remove those
                value = re.sub(r"\[nb \d\]", "", value)

                # New Horizons only northern hemisphere
                if "South" in value:
                    value = re.sub(r'South.*', "", value)
                    value = re.sub(r"North:", "", value).strip()

                # New Leaf Tortimer island check
                if "Tortimer Island" in value:
                    infobox_data["tortimer_island"] = True
                    infobox_data["tortimer_island_exclusive"] = False
                    # Different formatting
                    if "All year (Tortimer Island)" in value:
                        # Remove from string, only keep mainland months
                        value = value.replace("All year (Tortimer Island)", "")
                    elif value == "All year (also available on Tortimer Island)":
                        # Mainland and tortimer island months same, just keep all year
                        value = "All year"
                    elif value == "All year (only on Tortimer Island)":
                        value = "All year"
                        infobox_data["tortimer_island_exclusive"] = True
                else:
                    infobox_data["tortimer_island"] = False

                # Placeholder for critters with unknown date
                if value == "Unknown":
                    value = "Feb"

                if value.lower() == "all year":
                    value = "Jan – Dec"

                # Months can have disjoint timeframes, these are usually split with a ; or & (e.g. Mar – Jun; Sep)
                split_values = re.split(r"[&;]", value)
                for timeframe in split_values:
                    infobox_data["months_available"].extend(month_range_to_month_numbers(timeframe))
                
                # Sort for neatness
                infobox_data["months_available"] = sorted(infobox_data["months_available"])
            elif name == "Time of day":
                # Use dict to keep track of all available hours per month, as
                # hours can differ per month
                infobox_data["time_available"] = {}

                if value == "All day":
                    for month in infobox_data["months_available"]:
                        infobox_data["time_available"][month] = [h for h in range(0, 24)]
                else:
                    # Match time pattern like 8 AM – 7 PM (spaces optional)
                    time_pattern = r"^\d{1,2}\s?(AM|PM)\s?–\s?\d{1,2}\s?(AM|PM)$"

                    # Match time pattern ending with month(s) between parentheses
                    # (e.g. 8 AM – 7 PM (Jun) or 8 AM – 5 PM (Jul – Aug))
                    month_end_pattern = r"\d{1,2}\s?(?:AM|PM)\s?–\s?\d{1,2}\s?(?:AM|PM)\s?\([A-z]{3}(?:\s?–\s?[A-z]{3})?\)"

                    # Match time pattern where string is formatted like
                    # Mar – Jun:8 AM – 4 PMSep:8 AM – 4 PM
                    month_start_pattern = r"[A-z]{3}(?:\s?–\s?[A-z]{3})?:\s?\d{1,2}\s?(?:AM|PM)\s?–\s?\d{1,2}\s?(?:AM|PM)"

                    # Remove tortimer island times if present, will do this later
                    value = re.sub(r"Tortimer Island.*", "", value)

                    # Tortimer island critters with only one other availability
                    # show hours under 'mainland' header, remove this so we are
                    # left with a single hour range (works because we also remove
                    # tortimer island part above)
                    value = value.replace("Mainland:", "")

                    # Some times have footnotes, remove those
                    value = re.sub(r"\[nb \d\]", "", value)

                    # Time available has 3 formats
                    # Easy format, one time range for all months
                    if re.match(time_pattern, value.strip()):
                        hour_range = hour_range_to_hour_numbers(value)
                        # Same list for every month, but needed for compatability
                        # with critters that have different times per month
                        for month in infobox_data["months_available"]:
                            infobox_data["time_available"][month] = hour_range
                    # Times are formatted like Mar – Jun:8 AM – 4 PMSep:8 AM – 4 PM
                    elif matches := re.findall(month_start_pattern, value):
                        for match in matches:
                            months, hours = match.split(":")
                            
                            # Transform string ranges to int ranges
                            month_range = month_range_to_month_numbers(months.strip())
                            hour_range = hour_range_to_hour_numbers(hours.strip())

                            for month in month_range:
                                infobox_data["time_available"][month] = hour_range
                    # Times are formatted like '8 AM – 7 PM (Jun)  8 AM – 5 PM (Jul – Aug)'
                    elif matches := re.findall(month_end_pattern, value):
                        for match in matches:
                            hours = re.search(time_pattern[:-1], match).group(0)
                            months = re.sub(time_pattern[:-1], "", match).strip()

                            # Transform string ranges to int ranges
                            month_range = month_range_to_month_numbers(months)
                            hour_range = hour_range_to_hour_numbers(hours)
                            
                            for month in month_range:
                                infobox_data["time_available"][month] = hour_range
            elif name == "Location":
                infobox_data["location"] = value.strip()
            elif "Selling price" in name: # New Horizons is called selling prices
                # Flick/CJ price is always normal sell * 1.5 so we can remove it from data
                if "Flick" in value:
                    value = re.sub(r"Flick.*", "", value)
                if "C.J." in value:
                    value = re.sub(r"C.J.*", "", value)

                # Price is comma separated and can contain text, use regex to remove
                # everything that is not a number
                value = re.sub(r"\D", "", value)
                
                infobox_data["selling_price"] = int(value)
            # Only for new horizons
            elif name == "Spawn requirement":
                infobox_data["spawn_requirement"] = value.strip()
            # Only for fish and sea creatures
            elif name == "Shadow size":
                infobox_data["shadow_size"] = value.strip()
            # Only for sea creatures
            elif name == "Shadow movement":
                infobox_data["shadow_movement"] = value.strip()        
            
        return infobox_data
