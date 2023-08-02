'''
單元測試框架
'''

import unittest

class TestStringMethods(unittest.TestCase):

    def test_calculation(self):
        aa = 25
        bb = 25
        self.assertEqual(aa * bb, 625)
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

    
