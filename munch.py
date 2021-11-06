'''
Munch App MVP
v.0.1
By Applause
The purpose of Munch is to create a dinner menu and to show the ingredients required
'''

# ------- Imports ------

from random import choice

# ------- A. Functions -------
# A1 - Choose dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu:)")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("Out of all these dishes, my fave has to be " + choice(myMenu) + ".")
    print()
    
# A2 - Build shopping list

def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Chicken Burgers" in myMenu:
        myShoppingList.append(chickenBurgers)
    if "Stir-fry Chicken" in myMenu:
        myShoppingList.append(stirFryChicken)
    if "ABC Soup" in myMenu:
        myShoppingList.append(ABCsoup)
    if "Fried Rice" in myMenu:
        myShoppingList.append(friedRice)
    if "Steamed Fish" in myMenu:
        myShoppingList.append(steamedFish)
    if "Noodles" in myMenu:
        myShoppingList.append(noodles)
    print()
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("You're done! Have fun!")

# -------- B. Lists ---------


foodWeLike = ["Pizza", "Chicken Burgers", "Stir-fry Chicken", "ABC Soup", "Fried Rice", "Steamed Fish", "Noodles"]

pizza = ["Pizza Base", "Tomato Sauce", "Cheese", "Pineapple", "Sausage", "Chillis"]
chickenBurgers = ["Minced Chicken", "Burger Buns", "Cheese"]
stirFryChicken = ["Chicken breast", "Soy Sauce", "Pepper", "Salt", "Sesame Oil"]
ABCsoup = ["Onion", "Potato", "Carrot", "Pork Ribs"]
friedRice = ["Rice", "Eggs", "Frozen Veg", "Sesame Oil", "Soy Sauce", "Sausage"]
steamedFish = ["Fish", "Fish Sauce", "Rock Sugar", "Mirin", "Ginger", "Garlic"]
noodles = ["noodles", "Egg"]


myMenu = []

#1. How many days to plan?

print("Hello, I'm Munch! I'll help you to plan your dinner menu")

answer = input("How many days would you like me to plan? ")
print()
print("Okay, I'm going to plan " + answer + " dinner(s) from your favourite meal list")

#2. Choose dishes

chooseDishes(answer)

#3. Build shopping list

answer = input("Would you like a shopping list for this menu? ")

if answer == 'y':
    buildShoppingList()
else:
    print("Happy eating!")
