import unittest
from unittest.mock import patch
from io import StringIO
from app import calculate_discount, price_basket

class TestPriceBasket(unittest.TestCase):

    def test_calculate_discount(self):
        item_counts = {'Apples': 3, 'Soup_Bread': 0}
        expected_discount = 0.30
        actual_discount = calculate_discount(item_counts)
        # Round both the expected and actual values to 2 decimal places for comparison
        self.assertAlmostEqual(expected_discount, actual_discount, places=2)

    def test_price_basket(self):
        basket = ['Soup', 'Bread', 'Milk', 'Apples']  # Updated basket list
        expected_output = "Subtotal: £3.75\nSoup_Bread Buy 2 tins of soup and get a loaf of bread for half price: £0.00\nApples 10% off: £0.10\nTotal price: £3.65\n"

        with patch('sys.argv', ['app.py'] + basket):  # Mock command-line arguments
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                price_basket(basket)

        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
