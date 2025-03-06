import unittest
from src.bot import start

class TestBot(unittest.TestCase):
    def test_start(self):
        """Verifica se a função start está definida."""
        self.assertIsNotNone(start)

if __name__ == '__main__':
    unittest.main()
