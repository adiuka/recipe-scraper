from recipe_to_csv import recipe_to_csv
from link_scraper import link_scraper

recipe_links = link_scraper()
recipe_to_csv(recipe_links)
