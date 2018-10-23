from part import Part
from parse import Parse
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the format functions of the parser.
    """
    def test_format_one(self):
        input_line = 'TSR-1002:Panasonic:A1,D2'
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertEqual(part.mpn, 'TSR-1002')
        self.assertEqual(part.manufacturer, 'Panasonic')
        self.assertEqual(part.reference_designators, ['A1','D2'])

    def test_format_two(self):
        return

    def test_format_three(self):
        return

    def test_empty_line(self):
        input_line = ''
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertIsNone(part)

    def test_mangled_input(self):
        input_line = 'TSR---10302:Panaso;;frrk:A1,D2,2;'
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertIsNone(part)

if __name__ == '__main__':
    unittest.main()