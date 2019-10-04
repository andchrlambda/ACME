import random
from random import randint

class Product:
    """ Writing python class for Acme (Part 1 - Keeping it Classy)"""

    def __init__(self, name=None, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

        # Adding methods
    def stealability(self):
        """Calculates how whether a Product will be stolen
        based on price and weight."""
        ratio = self.price/self.weight
        if ratio < 0.5:
            return print("Not so stealable...")
        elif 1 > ratio >= 0.5:
            return print("Kinda stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        """Calculates a Product's liklihood to combust based on
        flammability and weight."""
        product = self.flammability * self.weight
        if product < 10:
            return print("fizzle")
        elif  50 > product >= 10:
            return print("boom!")
        else:
            print("BABOOM!!")

class BoxingGlove(Product):
    """Defines a Boxing Gloves as a subset of Products for Acme."""
    def __init__(self, name, price =10, weight=10, flammability=0.5):
        super().__init__(self, name, price, weight, flammability)


    def explode (self):
        return print("It's a glove.")

    def punch (self):
        if self.weight < 5:
            return print("That tickles.")
        elif  15 > product >= 5:
            return print("Hey, that hurt!")
        else:
            print("OUCH!!")
