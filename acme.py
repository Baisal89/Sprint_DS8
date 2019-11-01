from random import randint

class Product(object):
    """ACME product"""

    def __init__(self, name: str, price: int = 10,
                 weight: int = 20.0, flammability: float = 0.5):

                 self.name = name
                 self.price = price
                 self.weight = weight
                 self.flammability = flammability
                 self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """calculating stealability of product"""

        """stealability = price/weight"""

        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stable...'

        if 0.5 <= steal < 1:
            return 'Kinda stealable.'
        return 'Very Stable!'

    def explode(self):
        """ Calculating explodability of product"""

        """explodability = flammability * self.weight"""

        stable = self.flammability * self.weight
        if stable < 10:
            return '...fizzle'
        if 10 <= stable < 50:
            return '...boom!'
        return '...BABOOM'


    class BoxingGlove(Product):
        """ACME Boxing Glove"""

        def __init__(self, name: str, price: int = 10,
                     weight: int = 10, flammability: float = 0.5):
                     super(BoxingGlove, self).__init__(name=name,
                                                       price=price,
                                                       weight=weight,
                                                       flammability=flammability)

        def explode(self):
            """This product can not explode"""

            return '...it\'s a glove'

        def punch(self):
            """Calculating punch strength of glove"""

            if self.weight > 5:
                return 'That tickles'
            if 5 <= self.weight < 15:
                return 'Hey that hurt!'
            return 'OUCH!'


if __name__ == "__main__":
    pass
