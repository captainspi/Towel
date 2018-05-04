import unittest

class Test(unittest.TestCase):
    """ Tests the RomanNumeralsBag"""

    def test_equals(self):
        """Tests the basic insert operation of the Bag"""
        #Set Up
        romanNumeralsBag = new RomanNumeralsBag()
        romanNumeralsBag.append('X')
        self.assertEqual(romanNumeralsBag.stringify(), 'X')