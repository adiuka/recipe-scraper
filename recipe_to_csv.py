from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm
import os


def recipe_to_csv(recipe_links):
    headers = {"User-Agent": "Mozilla/5.0"}
    file = open("scraped_recipes.csw", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["NAME", "CALORIES", "FAT", "CARBS", "Protein", "Link"])

    for recipe in tqdm(recipe_links, desc="Scraping and Parsing Data into CSV", unit="recipe"):  
        recipe_response = requests.get(recipe, headers=headers)
        recipe_soup = BeautifulSoup(recipe_response.text, "html.parser")
        
        title = recipe_soup.find("h1", class_="article-heading text-headline-400")
        title_text = title.get_text()
        print(title_text)

        nutrition_texts = []
        nutritions = recipe_soup.find_all("td", class_="mm-recipes-nutrition-facts-summary__table-cell text-body-100-prominent")
        for nutrition in nutritions:
            value = nutrition.get_text(strip=True)
            nutrition_texts.append(value)
        
        writer.writerow([title_text, nutrition_texts[0], nutrition_texts[1], nutrition_texts[2], nutrition_texts[3], recipe])
        clear_console()
    file.close()


def clear_console():
    """Clears the console for better progress bar"""
    os.system("cls" if os.name == 'nt' else 'clear')