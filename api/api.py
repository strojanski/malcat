from flask import Flask, request, jsonify
from scraper import *
import json
import re

app = Flask(__name__)

URL = "https://www.studentska-prehrana.si/sl/restaurant/Details/"
places = json.loads(open("restaurants.json", "r", encoding="utf-8").read())["restaurants"]

@app.route("/api/v1/restaurant/<int:id>", methods=["GET"])
def get_menu_by_id(id: int):
    restaurant = Restaurant(URL)
    
    menu = restaurant.get_menu(id)
    
    full_price, student_price = restaurant.get_prices(id)
    
    meals = []
    for meal in menu:
        meals.append(re.sub(r'\\u0[\da-fA-F]{2}', "", meal.get_text(strip=True)))
        
    
    return jsonify({
        "full_price:" : full_price,
        "student_price" : student_price,
        "meals" : meals
    })


if __name__ == "__main__":
    app.run(debug=True)
