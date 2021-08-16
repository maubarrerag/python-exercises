import unittest
from Die import Die

class TestDie(unittest.TestCase):
    

    def setUp(self):
        self.Die1 = Die(6)
        self.Die2 = Die(-1)
    
    def test_range(self):
        self.assertTrue(self.Die1.roll() <= 6)
        self.assertGreaterEqual(self.Die1.roll(), 0)
        self.assertIsNone(self.Die2.roll())