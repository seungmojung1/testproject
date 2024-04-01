MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
money = 0


def check_resource(choice):
    for i in choice['ingredients']:
        if resources[i] < choice['ingredients'][i]:
            return print(f"Sorry there is not enough {i}.")
    return insert_coin(choice, choice['cost'])


def insert_coin(menu, price):
    global money
    print("Please insert coins.")
    q = int(input("how many quarters?"))
    d = int(input("how many dimes?"))
    n = int(input("how many nickles?"))
    p = int(input("how many pennies?"))

    total = (q*0.25) + (d*0.10) + (n*0.05) + (p*0.01)
    if price > total:
        return print("Sorry that's not enough money. Money refunded.")
    elif price < total:
        print(f"Here is ${round(total - price, 2)} in change.")
        make_coffee(menu)
        money += price
    else:
        make_coffee(menu)
        money += price


def make_coffee(menu):
    global userInput
    for i in menu['ingredients']:
        # print(menu['ingredients'][i])
        resources[i] -= menu['ingredients'][i]
    print(f"Here is your {userInput} ☕️. Enjoy!")


while is_on:
    userInput = input("What would you like? (espresso/latte/cappuccino):")
    if userInput == "off":
        is_on = False
    elif userInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        check_resource(MENU[userInput])
