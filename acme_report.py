from random import uniform, randint, choice
from acme import Product


DJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n: int = 30) -> list:
    """Creating list of new ACME products!"""

    products = []

    for i in range(n):
        name = choice(DJECTIVES) + ' ' + choice(NOUNS)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name, price=price, weight=weight,
                                flammability=flammability))

    return products


def inventory_report(products: list) -> None:
    """ACME inventory report"""

    names = len(set([prod.name for prod in products]))
    list_len = len(products)
    ave_weight = sum([prod.weight for prod in products])/list_len
    ave_price = sum([prod.price for prod in products])/list_len
    ave_flame = sum([prod.flammability for prod in products])/list_len

print('\n OFFICIAL ACME INVENTORY REPORT:\n')
print(f'Number of unique product names: {names}')
print(f'Mean product weight: {ave_weight:.2f}')
print(f'Mean product price: {ave_price:.2f}')
print(f'Mean product flammability: {ave_flame:.2f}')


if __name__ =="__main__":
    inventory_report(generate_products())
