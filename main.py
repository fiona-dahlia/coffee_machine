from coffee_resources import MENU

def report(resource_list):
    print(f'Water: {resource_list["water"]}ML')
    print(f'Milk: {resource_list["milk"]}ML')
    print(f'Coffee: {resource_list["coffee"]}G')
    print(f'Money: ${resource_list["money"]}0')


def resource_sufficient(material, chosen_drink):
    ingredients_needed = MENU[chosen_drink]["ingredients"]
    for ingredient in ingredients_needed:
        # print(f"ingredient: {ingredient}")
        if material[ingredient] < ingredients_needed[ingredient]:
            return False
    return True


def process_coins():
    total_money = int(input("how many quarters?: ")) * 0.25
    total_money += int(input("how many dimes?: ")) * 0.1
    total_money += int(input("how many nickles?: ")) * 0.05
    total_money += int(input("how many pennies?: ")) * 0.01
    return total_money


def make_coffee(chosen_drink, ingredients, materials):
    for ingredient in ingredients:
        materials[ingredient] -= ingredients[ingredient]
    print("Here is your drink, enjoy!")


def transaction_successful(received_money, cost_of_drink):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if received_money >= cost_of_drink:
        change = round(received_money - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.00,
    }
    is_machine_on = True
    while is_machine_on:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "off":
            return
        elif drink == "report":
            report(resources)
        else:
            if resource_sufficient(resources, drink):
                money = process_coins()
                # print(money)
                if transaction_successful(money, MENU[drink]["cost"]):
                    resources["money"] += MENU[drink]["cost"]
                    make_coffee(drink, MENU[drink]["ingredients"], resources)
            else:
                print("Sorry, not enough resources to make your drink.")


coffee_machine()
