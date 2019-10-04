import unittest
from acme import Productsfrom acme_report import generate_products, ADJECTIVES,
NOUNS

class AcmeProductTests(unittest.TestCase):
    """test the class"

    def test_default_product_price(self):
        """Test default product price is 10."""
        prod = Product("Test Product")
        self.assertEqual(prod.price, 10)

if__name__=='__main__':
    unittest.main()
