

from bs4 import BeautifulSoup as bs
import requests
import json
import os

restaurants = open("restaurants.json", "r", encoding="utf-8")
restaurants = restaurants.read()
restaurants = json.loads(restaurants)
restaurants = restaurants["restaurants"]

URL = "https://www.studentska-prehrana.si/sl/restaurant/Details/"

class Restaurant:
    def __init__(self, url):
        self.url = url
        
    def get_menu(self, restaurant_id):
        res = requests.get(self.url + str(restaurant_id))       
        soup = bs(res.content, "html.parser")
        
        return soup.find_all("strong", class_="color-blue")
        
    def get_prices(self, restaurant_id):
        res = requests.get(self.url + str(restaurant_id))       
        soup = bs(res.content, "html.parser")
        
        prices = soup.find_all("span", class_="color-light-grey")
        student_price = prices[0].get_text(strip=True)
        full_price = prices[1].get_text(strip=True)
        
        return full_price, student_price


if __name__ == "__main__":
    rest = Restaurant(URL)
    
    for restaurant in restaurants:
        print(restaurant["name"])
        menu = rest.get_menu(restaurant["id"])
        print(f"Full price: {rest.get_prices(restaurant['id'])[0]}, student price: {rest.get_prices(restaurant['id'])[1]}\n")
        for meal in menu:
            print(meal.get_text(strip=True))
            
        print("\n")
