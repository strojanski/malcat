

from bs4 import BeautifulSoup as bs
import requests
import json
import os

restaurants = open("restaurants.json", "r", encoding="utf-8")
restaurants = restaurants.read()
restaurants = json.loads(restaurants)
restaurants = restaurants["restaurants"]

URL = "https://www.studentska-prehrana.si/sl/restaurant/Details/"


for restaurant in restaurants: 
    print(restaurant["name"])
    res = requests.get(URL + str(restaurant["id"]))
    soup = bs(res.content, "html.parser")

    # All menus are in strong color-blue
    menu = soup.find_all("strong", class_="color-blue")

    #print(menu)
    for food in menu:
        food = food.get_text(strip=True)
        print(food)
    print("\n")
