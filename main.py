import csv
from datetime import datetime


class Pizza:
    def __init__(self):
        self.description = " "
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Classic(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 80


class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 110


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Pizza Turko"
        self.cost = 110


class PlainPizza(Pizza):
    def __init__(self):
        self.description = "Plain Pizza"
        self.cost = 70

    # Decorator class and subclasses used to dynamically add additional behavior to a pizza object


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olives(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Olives"
        self.cost = 5


class Mushrooms(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mushrooms"
        self.cost = 7


class GoatCheese(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Goat Cheese"
        self.cost = 13


class Meat(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Meat"
        self.cost = 17


class Onions(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Onions"
        self.cost = 4


class Corn(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Corn"
        self.cost = 6


def get_pizza(list, n, list2, m):
    pizza = list[n]
    pizza = list2[m](pizza)
    return pizza
def main():
    # Read menu from text file
    with open("Menu.txt", "r") as f:
        menu = f.read()
        menux = f.readlines()

    print(menu)
    # Prompt user to choose pizza and sauce
    pizza_choice = int(input("Enter pizza choice: "))
    sauce_choice = int(input("Enter sauce choice: "))

    list = [Classic(), Margherita(), TurkPizza(), PlainPizza()]

    list2 = [Olives, Mushrooms, GoatCheese, Meat, Onions, Corn]
    pizza = get_pizza(list, pizza_choice, list2, sauce_choice)

    # Get the total cost of the pizza with sauce
    total_cost = pizza.get_cost()
    print('Total Cost is :', total_cost)
    # Get user information
    name = input("Please enter your name: ")
    id_num = input("Please enter your ID number: ")
    cc_num = input("Please enter your credit card number: ")
    cc_password = input("Please enter your credit card password: ")

    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%m-%d %H:%M:%S")

    # Save the order to the database file
    with open("Orders_Database.csv", mode="a") as db:
        saver = csv.writer(db)
        saver.writerow([name, id_num, cc_password, cc_num, pizza.get_description(), current_time, total_cost])

    print("\nThank you for your order!")

main()
