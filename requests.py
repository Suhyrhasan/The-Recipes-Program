"""
All functions access associated url, convert data from JSON format into
something usable, and returns that data as a corresponding object
"""

from urllib import request, parse
import json

from objects import Category, Area, Meal, Recipe


def get_categories():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for category_data in data["meals"]:
            category = Category(category_data["strCategory"])

            categories.append(category)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories


def print_categories():
    category = get_categories()

    print("Areas")
    for i in range(len(category)):
        category = category[i]
        print(" " + category.get_category())


def get_areas():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for area_data in data["meals"]:
            area = Area(area_data["strArea"])

            areas.append(area)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return areas


def print_areas():
    area = get_areas()

    print("Areas")
    for i in range(len(area)):
        area = area[i]
        print(" " + area.get_area())


def get_meals_by_category(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = request.urlopen(url)
    category_meals = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for meal_data in data["meals"]:
            category_meal = Meal(meal_data["strMeal"])

            category_meals.append(category_meal)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return category_meals


def print_category_meals():
    category_meals = get_meals_by_category("Seafood")

    print("Meals by Category")
    for i in range(len(category_meals)):
        meal = category_meals[i]
        print(" " + meal.get_meal())


def get_meals_by_area(area):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    f = request.urlopen(url)
    area_meals = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for meal_data in data["meals"]:
            area_meal = Meal(meal_data["strMeal"])

            area_meals.append(area_meal)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return area_meals


def print_area_meals():
    area_meals = get_meals_by_area("Canadian")

    print("Meals by Area")
    for i in range(len(area_meals)):
        meal = area_meals[i]
        print(" " + meal.get_meal())


def get_meal_by_name(meal):

    if meal == "random":
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
    else:
        url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(meal)
    f = request.urlopen(url)
    recipe = ""

    try:
        data = json.loads(f.read().decode("utf-8"))
        for recipe_data in data["meals"]:
            recipe = Recipe(recipe_data["strMeal"], recipe_data["strInstructions"],
                            recipe_data["strIngredient1"], recipe_data["strIngredient2"],
                            recipe_data["strIngredient3"], recipe_data["strIngredient4"],
                            recipe_data["strIngredient5"], recipe_data["strIngredient6"],
                            recipe_data["strIngredient7"], recipe_data["strIngredient8"],
                            recipe_data["strIngredient9"], recipe_data["strIngredient10"],
                            recipe_data["strIngredient11"], recipe_data["strIngredient12"],
                            recipe_data["strIngredient13"], recipe_data["strIngredient14"],
                            recipe_data["strIngredient15"], recipe_data["strIngredient16"],
                            recipe_data["strIngredient17"], recipe_data["strIngredient18"],
                            recipe_data["strIngredient19"], recipe_data["strIngredient20"],
                            recipe_data["strMeasure1"], recipe_data["strMeasure2"],
                            recipe_data["strMeasure3"], recipe_data["strMeasure4"],
                            recipe_data["strMeasure5"], recipe_data["strMeasure6"],
                            recipe_data["strMeasure7"], recipe_data["strMeasure8"],
                            recipe_data["strMeasure9"], recipe_data["strMeasure10"],
                            recipe_data["strMeasure11"], recipe_data["strMeasure12"],
                            recipe_data["strMeasure13"], recipe_data["strMeasure14"],
                            recipe_data["strMeasure15"], recipe_data["strMeasure16"],
                            recipe_data["strMeasure17"], recipe_data["strMeasure18"],
                            recipe_data["strMeasure19"], recipe_data["strMeasure20"])

    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return recipe


# def display_meal(recipe):


def print_meal(recipe):
    recipe = get_meal_by_name(recipe)
    print()
    print("Recipe: ", recipe.get_meal())
    print()


# main function for testing API calls
def main():
    print_area_meals()


if __name__ == '__main__':
    main()
