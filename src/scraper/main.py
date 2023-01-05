if __name__ == "__main__":
    import logging
    from tqdm import tqdm
    from src.scraper.critterpage import CritterPage
    from src.scraper.database import CritterDatabase
    from src.scraper.utils import get_critter_list_from_url, url_blacklist, db_path

    logging.basicConfig()

    list_page_urls = [
        "https://nookipedia.com/wiki/Bug",
        "https://nookipedia.com/wiki/Fish",
        "https://nookipedia.com/wiki/Sea_creature",
    ]

    critter_urls = []
    for url in list_page_urls:
        critter_urls.extend(get_critter_list_from_url(url))

    critter_urls = [url for url in critter_urls if url not in url_blacklist]

    critter_pages = [CritterPage(url) for url in tqdm(critter_urls, desc="Scraping infoboxes")]
    
    infoboxes = []
    for page in critter_pages:
        infoboxes.extend(page.infoboxes)

    db = CritterDatabase(db_path)

    for infobox in tqdm(infoboxes, desc="Inserting rows"):
        db.insert_row(infobox)

    db.close()
