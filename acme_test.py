import unittest
from acme import Product
from acme_report import generate_products, DJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):


    def setUp(self) -> None:
        """Creating defult product and one with changed defautls"""

        self.default = Product('Test Product')
        self.tester = Product('Tester', price=15, weight=2)


    def test_default_product_price(self):
        """ Default is 10"""
        self.assertEqual(self.default.price, 10)


    def test_default_product_weight(self):
        """Default is 20"""

        self.assertEqual(self.default.weight, 20)


    def test_tester_price(self):
        """Price is 15"""
        self.assertEqual(self.tester.price, 15)


    def test_tester_weight(self):
        """Weight is 2"""
        self.assertEqual(self.tester.weight, 2)

    def test_tester_steability(self):
        """stealability is 2"""
        self.assertEqual(self.tester.stealability(), 'Very steable!')

    def test_tester_explode(self):
        """Explode if it equal to 1.25"""
        self.assertEqual(self.tester.explode(), '...fizzle')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        names = [prod.name for prod in generate_products()]
        sep = [(name.split()[0], name.split()[1], for name in names)]
        for name in sep:
            self.assertIn(name[0], DJECTIVES)
            self.assertIn(name[1], NOUNS)

if __name__=='__main__':
    unittest.main()
