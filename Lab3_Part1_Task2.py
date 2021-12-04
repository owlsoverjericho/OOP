import os
from random import randint
clear = lambda: os.system('cls')


class Pizza:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

margarita = Pizza("Pizza Margarita", "189", ["Mozarella", "Tomato sauce"])

pepperoni = Pizza("Pizza Pepperoni", "214", ["Mozarella", "Peperoni", "Tomato sauce"])

bbq = Pizza("Pizza BBQ", "214", ["Chicken", "Onion", "Bacon", "Mushrooms", "Mozarella", "BBQ sauce"])

hawaiian = Pizza("Hawaiian Pizza", "214", ["Chicken", "Pineapple", "Mozarella", "Tomato sauce"])

texas = Pizza("Pizza Texas", "189", ["Corn", "Onion", "Mushrooms", "Bavarian sausages", "Mozarella", "BBQ sauce"])

country = Pizza("Pizza Country", "235", ["Onion", "Bacon", "Ham", "Mushrooms", "Mozarella", "Pickled" "cucumbers", "Garlic sauce"])

carbonara = Pizza("Pizza Carbonara", "235", ["Onion", "Bacon", "Ham", "Mushrooms", "Mozarella", "Al'fredo sauce"])

pizzas = [margarita, pepperoni, bbq, hawaiian, texas, country, carbonara]


def addIngredients(pizzas, day):
    customPizza = pizzas[day]
    index = 0
    for ingredient in customPizza.ingredients:
        print(f"{index}: Add extra {ingredient}")
        index += 1;
    try:
        userInput = int(input("Choose an option: "))
    except ValueError as error:
        print("Incorrect input! Try again ", error, sep='\n')
    else:
        if (userInput >= 0 and userInput <= index):
            clear()
            customPizza.ingredients.append(customPizza.ingredients[userInput])
            print(f"Added extra {customPizza.ingredients[userInput]} to your pizza!")

def menu(pizzas, day):
        orderStatus = False
        print("1: Show ingredients\n2: Show price\n3: Add ingredients\n4: Buy pizza\n5: Show my order\n6: Exit")
        while True:
            try:
                userInput = int(input("Choose an option: "))
            except ValueError as error:
                clear()
                print("Incorrect input! Try again ", error, sep='\n')
                menu(pizzas, day)
            else:
                if (userInput == 1):
                    clear()
                    print("The ingredients are: ")
                    print(", ".join(pizzas[day].ingredients))
                    menu(pizzas, day)
                elif (userInput == 2):
                    clear()
                    print("The price is:", pizzas[day].price)
                    menu(pizzas, day)
                elif (userInput == 3):
                    clear()
                    addIngredients(pizzas, day)
                    menu(pizzas, day)
                elif (userInput == 4):
                    clear()
                    print(f"Added {pizzas[day].name} to your order!")
                    menu(pizzas, day)
                elif (userInput == 5):
                    clear()
                    print(f"Item: {pizzas[day].name}\nPrice: {pizzas[day].price}\nIngredients: {', '.join(pizzas[day].ingredients)}")
                    menu(pizzas, day)
                elif (userInput == 6):
                    break
                else:
                    clear()
                    print("Please choose a valid option!")
                    menu(pizzas, day)
def main():
    day = randint(0, 6)    
    print(f"Todays Pizza Of The Day is {pizzas[day].name}!")
    menu(pizzas, day)

main()


