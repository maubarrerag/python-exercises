def prepend(s,c):
    return c + s

def append(s,c):
    return s + c

def insert(s,c,pos):
    return s[0:pos] + c + s[pos:-1] #wrong

import unittest

class TestMyMethods(unittest.TestCase):
    def test_prepend(self):
        self.assertEqual(prepend('bar','foo'), 'foobar')
    def test_append(self):
        self.assertEqual(append('bar','foo'), 'barfoo')
    def test_insert(self):
        self.assertEqual(insert('wetor','buca',2), 'webucator')

suite = unittest.TestLoader().loadTestsFromTestCase(TestMyMethods)
unittest.TextTestRunner().run(suite)