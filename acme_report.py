"""Acme Inventory Report"""
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

#price and weight range from 5-100 (as integers)
# flammability ranges from 0.0 = 2.5 (as float)

products = []
def generate_products():
    """Generate a random list of 30 products."""
    for item in range (random.randint(0,30)):
        products.append(item)

    return #list with column names

# number of unique product names
# averages for: price, weight, and flammability

def inventory_report():
    """Print a summary of products."""
    "Print an inventory report with useful information."
    avg_price = sum(product.price)/len(product.price) #where price is a column name


print("Following is a useful starting code for acme_report.py Python #!/usr/bin/env python")
