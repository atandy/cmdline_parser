from part import Part
from parse import Parse
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_format_one(self):
        input_line = 'TSR-1002:Panasonic:A1,D2'
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertEqual(part.mpn, 'TSR-1002')
        self.assertEqual(part.manufacturer, 'Panasonic')
        self.assertEqual(part.reference_designators, ['A1','D2'])

    def test_empty_line(self):
        input_line = ''
        parser = Parse(input_line)
        parse_result = parser.parse_bom_line()
        self.assertIsNone(parse_result)


    def test_mangled_input(self):
        input_line = 'TSR---10302:Panaso;;frrk:A1,D2,2;'
        parser = Parse(input_line)
        parse_result = parser.parse_bom_line()
        self.assertIsNone(parse_result)


if __name__ == '__main__':
    unittest.main()
    '''
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')
    '''
