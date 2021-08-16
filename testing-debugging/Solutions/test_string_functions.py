import unittest
from string_functions import *

class TestStringFunctions(unittest.TestCase):
    
    def test_prepend(self):
        self.assertEqual(prepend('bar','foo'), 'foobar')
        
    def test_append(self):
        self.assertEqual(append('bar','foo'), 'barfoo')
        
    def test_insert(self):
        self.assertEqual(insert('wetor','buca',2), 'webucator')
    
    def test_remove_non_ascii_letters(self):
        test = remove_non_ascii_letters('HO	g+)JH*cM_EQZ<JzG')
        self.assertEqual(test,'HOgJHcMEQZJzG')
        
    def test_discover_email(self):
        test = discover_email('bill-at-example-dot-com')
        self.assertEqual(test, 'bill@example.com')

    def test_inits(self):
        self.assertEqual(inits('Monty Hall Python'), 'M.H.P.')

if __name__ == '__main__':
    unittest.main()