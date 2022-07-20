from coffee_resources import MENU


def report(resource_list):
    print(f'Water: {resource_list["water"]}')
    print(f'Milk: {resource_list["milk"]}')
    print(f'Coffee: {resource_list["coffee"]}')


# TODO: .4 Check resources sufficient.
def resource_sufficient(resources, chosen_drink):
    ingredients_needed = MENU[chosen_drink]["ingredients"]
    for ingredient in ingredients_needed:
        print(f"ingredient: {ingredient}")
        if resources[ingredient] < ingredients_needed[ingredient]:
            return False
        else:
            return True


def process_coins():
    coins = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickle": 0.05,
        "penny": 0.01,
    }



def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.00,
    }

    # TODO: .1 Prompt user by asking “What would you like?".
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: .2 Turn off the Coffee Machine by entering “off” to the prompt.
    if drink == "off":
        return
    # TODO: .3 Print report.
    elif drink == "report":
        report(resources)
    else:
        has_resources = resource_sufficient(resources, drink)
        print(f"has_resources: {has_resources}")

    # TODO: .5 Process coins
    # TODO: .6 Check if transaction successful.
    # TODO: .7 Make Coffee.


coffee_machine()
