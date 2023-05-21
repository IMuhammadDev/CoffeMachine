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
money = 1000
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarter = 0.25
dime = 0.1
nickle = 0.05
penni = 0.01


def payment(selected):
    result = False
    qwt = int(input("How many quarters?: "))
    dm = int(input("How many dimes?: "))
    nick = int(input("How many nickles?: "))
    penn = int(input("How many pennies?: "))
    accepted = (qwt * quarter) + (dm * dime) + (nick * nickle) + (penn * penni)
    if MENU[selected]["cost"] <= accepted:
        print(f"Here is {accepted} in change")
        if MENU[selected]["cost"] < accepted:
            back = accepted - MENU[selected]["cost"]
            print(f"Welcome your back {back}$")
        result = True
        return result
    else:
        print("your payment is not enough")
        return result


def check_recourse(chosen):
    not_enough = 'Sorry there is not enough '
    if chosen == " espresso":
        result_water = resources["water"] - MENU[chosen]["ingredients"]["water"]
        result_coffee = resources["coffee"] - MENU[chosen]["ingredients"]["coffee"]
        if result_water <= 0:
            not_enough += "water "
        if result_coffee <= 0:
            not_enough += "coffe."
        return not_enough
    else:
        result_water = resources["water"] - MENU[chosen]["ingredients"]["water"]
        result_coffe = resources["coffee"] - MENU[chosen]["ingredients"]["coffee"]
        result_milk = resources["milk"] - MENU[chosen]["ingredients"]["milk"]

        if result_water <= 0:
            not_enough = not_enough + "water "
        if result_coffe <= 0:
            not_enough += "coffee "
        if result_milk <= 0:
            not_enough += "milk."
        return not_enough


def take_an_order(selected):
    if check_recourse(selected) != 'Sorry there is not enough ':
        print(check_recourse(selected))
    else:
        if payment(selected=selected):
            print(f"Here is your {selected} Enjoy")


print("Welcome to the Coffee Machine!")
condition = True
while condition:
    selection = input("What would you like (espresso , late , cappuccino )")
    if selection == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"money: {money}")
        continue
    else:
        take_an_order(selected=selection)
