import unittest
from src.payments import get_balance, create_invoice

class TestPayments(unittest.TestCase):
    def test_get_balance(self):
        response = get_balance()
        self.assertIn('ok', response)

    def test_create_invoice(self):
        response = create_invoice(1)
        self.assertIn('ok', response)

if __name__ == '__main__':
    unittest.main()
