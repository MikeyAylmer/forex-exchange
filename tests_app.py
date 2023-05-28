from unittest import TestCase
from app import app
from forex_python.converter import RatesNotAvailableError
from forex_methods import curr_converter, convert_symbol, round_currency, cat_curr_symbol

class ForexAppPythonMethods(TestCase):
    def test_curr_converter(self):
        self.assertEqual(curr_converter('USD', 'USD', 1), 1.0)
        self.assertEqual(curr_converter('USD', 'USD', 1.9473), 1.9473)
        self.assertRaises(RatesNotAvailableError, curr_converter, 'URE', 'USD', 200)

    def test_convert_symbol(self):
        self.assertEqual(convert_symbol('USD'), '$')
        self.assertEqual(convert_symbol('EUR'), '€')
        self.assertEqual(convert_symbol('JPY'), '¥')

    def test_round_currency(self):
        self.assertEqual(round_currency(123.4567), 123.46)
        self.assertEqual(round_currency(45.7987), 45.80)

    def test_cat_curr_symbol(self):
        self.assertEqual(cat_curr_symbol('$', 45), '$45')
        self.assertEqual(cat_curr_symbol('¥', 200.26), '¥200.26')
