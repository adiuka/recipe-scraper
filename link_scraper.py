from bs4 import BeautifulSoup
from tqdm import tqdm
import requests

def link_scraper():
    """This functionretrieves the links found at the website"""
    page_to_scrape = "https://www.allrecipes.com/recipes/17561/lunch/" 
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(page_to_scrape, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    recipes = soup.find_all("a", class_="comp mntl-card-list-items mntl-universal-card mntl-document-card mntl-card card card--no-image")

    recipe_links = []

    for recipe in tqdm(recipes, desc="Scraping Recipe Links", unit="link"):
        href = recipe.get("href")
        recipe_links.append(href)
        
    return recipe_links