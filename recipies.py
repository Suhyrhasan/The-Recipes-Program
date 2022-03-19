import requests
import textwrap


def display_title():
    print("The Recipes Program")
    print()
    display_menu()


def list_categories(categories):
    print()
    print("CATEGORIES")
    for i in range(len(categories)):
        category = categories[i]
        print(" " + category.get_category())
    print()


def list_areas(areas):
    print()
    print("AREAS")
    for i in range(len(areas)):
        area = areas[i]
        print(" " + area.get_area())
    print()


# def list_meals_by_category():


def search_meal_by_category(categories):
    lookup_category = input("Enter a category: ")
    found = False
    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().title() == lookup_category.title():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals(meals, "category")
    else:
        print("That category does not exist in the database")


def search_meal_by_area(areas):
    lookup_area = input("Enter an area: ")
    found = False
    for i in range(len(areas)):
        area = areas[i]
        if area.get_area().title() == lookup_area.title():
            found = True
            break

    if found:
        meals = requests.get_meals_by_area(lookup_area)
        list_meals(meals, "area")
    else:
        print("That area does not exist in the database")


def list_meals(meal_list, title):
    print()
    print("LIST MEALS BY", title.upper())
    for i in range(len(meal_list)):
        meal = meal_list[i]
        print(" " + meal.get_meal())
    print()


def search_meal_by_name():
    lookup_meal = input("Enter the meal name: ")

    meal = requests.get_meal_by_name(lookup_meal)
    if meal:
        display_meal(meal)
    else:
        print("A recipe for that meal was not found.")


def display_meal(recipe):
    print()
    print("Recipe:", recipe.get_meal())
    print()

    my_wrap = textwrap.TextWrapper(width=100)
    wrap_list = my_wrap.wrap("Instructions: " + recipe.get_instructions())
    for line in wrap_list:
        print(line)

    print()
    print("Ingredients")
    print("-" * 100)

    ingredient_list = []
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure1(),
                                     recipe.get_ingredient1())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure2(),
                                     recipe.get_ingredient2())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure3(),
                                     recipe.get_ingredient3())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure4(),
                                     recipe.get_ingredient4())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure5(),
                                     recipe.get_ingredient5())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure6(),
                                     recipe.get_ingredient6())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure7(),
                                     recipe.get_ingredient7())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure8(),
                                     recipe.get_ingredient8())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure9(),
                                     recipe.get_ingredient9())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure10(),
                                     recipe.get_ingredient10())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure11(),
                                     recipe.get_ingredient11())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure12(),
                                     recipe.get_ingredient12())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure13(),
                                     recipe.get_ingredient13())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure14(),
                                     recipe.get_ingredient14())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure15(),
                                     recipe.get_ingredient15())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure16(),
                                     recipe.get_ingredient16())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure17(),
                                     recipe.get_ingredient17())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure18(),
                                     recipe.get_ingredient18())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure19(),
                                     recipe.get_ingredient19())
    ingredient_list = add_ingredient(ingredient_list, recipe.get_measure20(),
                                     recipe.get_ingredient20())

    col1 = ""
    col2 = ""
    col3 = ""
    i = 1
    for ingredient in ingredient_list:
        if i == 1:
            col1 = ingredient
        elif i == 2:
            col2 = ingredient
        elif i == 3:
            col3 = ingredient
            print("  {:30} {:30} {:30}".format(col1, col2, col3))
            col1 = ""
            col2 = ""
            col3 = ""
            i = 0
        i += 1

    if col1 != "":
        print("  {:30} {:30} {:30}".format(col1, col2, col3))
    print()


def add_ingredient(ingredient_list, measurement, ingredient):
    if ingredient is not None and ingredient != "":
        ingredient_line = "(" + measurement.strip() + ") " + ingredient.strip()
        ingredient_list.append(ingredient_line)
    return ingredient_list


def search_random():
    meal = requests.get_meal_by_name("random")
    if meal:
        display_meal(meal)


def display_menu():
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("0 - Exit the Program")
    print()


def main():
    display_title()
    categories = requests.get_categories()
    areas = requests.get_areas()

    while True:
        command = input("Command: ")
        if command == "1":
            list_categories(categories)
        elif command == "2":
            search_meal_by_category(categories)
        elif command == "3":
            search_meal_by_name()
        elif command == "4":
            search_random()
        elif command == "5":
            list_areas(areas)
        elif command == "6":
            search_meal_by_area(areas)
        elif command == "0":
            print("Thank you for dining with us!")
            break
        else:
            print("Invalid command. Try again please.")


if __name__ == '__main__':
    main()
