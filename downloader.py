from pinscrape.pinscrape.v2 import Pinterest
import asyncio

async def search_pinterest(keyword, limit=10):
    scraper = Pinterest()
    images_url = scraper.search(query=keyword, page_size=limit)
    # scraper.download(url_list=images_url, number_of_workers=1, output_folder="cats")
    return images_url
