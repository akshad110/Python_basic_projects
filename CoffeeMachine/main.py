import menu
import os

logo = """

 ________         __                                 __                          ___   ___                                        __     __                 
|  |  |  |.-----.|  |.----.-----.--------.-----.    |  |_.-----.    .----.-----.'  _|.'  _|.-----.-----.    .--------.---.-.----.|  |--.|__|.-----.-----.   
|  |  |  ||  -__||  ||  __|  _  |        |  -__|    |   _|  _  |    |  __|  _  |   _||   _||  -__|  -__|    |        |  _  |  __||     ||  ||     |  -__|__ 
|________||_____||__||____|_____|__|__|__|_____|    |____|_____|    |____|_____|__|  |__|  |_____|_____|    |__|__|__|___._|____||__|__||__||__|__|_____|__|

"""
profit = 0
resources = {
    "water":500,
    "milk":200,
    "coffee":100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! There is not enough {item}")
            return False
        return True
def process_coins():
    print("please insert coins (only 5rs,10rs,20rs coins accepted): ")
    total = 0
    coins_five = int(input("How many 5rs coins: "))
    coins_ten = int(input("How many 10rs coins: "))
    coins_twenty = int(input("How many 20rs coins: "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(user_payment, coffee_price):
    if user_payment >= coffee_price:
        global profit
        profit += coffee_price
        change = user_payment-coffee_price
        print(f"Here is your Rs{change} in change.")
        return True
    else:
        print("Sorry that's not enough money.money refunded.")
        return False

def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕... Enjoy!")

def coffee_machine():
    print(logo)
    choice = input(
        "what would you like to have? (latte/espresso/cappuccino),Type (off) to off the machine,Type (report) to get the report of the machine:\n ")
    os.system('cls')
    is_on = True
    while is_on:
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(
                f"Water: {resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:Rs {profit}")
        else:
            coffee_type = menu.Menu[choice]
            print(f"Coffee name: {choice}\nCoffee ingredients: {coffee_type}")
            if check_resources(coffee_type['ingredients']):
                payment = process_coins()
                if is_payment_successful(payment, coffee_type['cost']):
                    make_coffee(choice, coffee_type['ingredients'])
            coffee_machine()


coffee_machine()



