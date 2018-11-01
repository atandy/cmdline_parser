import unittest
from parse import Parse

class TestAdd(unittest.TestCase):
    """
    Test various methods from Parse class.
    """

    def test_format_one(self):
        """
        Test handling BOM format one.
        """
        input_line = 'TSR-1002:Panasonic:A1,D2'
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertEqual(part.mpn, 'TSR-1002')
        self.assertEqual(part.manufacturer, 'Panasonic')
        self.assertEqual(part.reference_designators, ['A1','D2'])

    def test_empty_line(self):
        """
        Test outcome of an empty line
        """
        input_line = ''
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertIsNone(part)

    def test_mangled_input(self):
        """
        Test outcome of mangled, multi-split input
        """
        input_line = 'TSR---10302:Panaso;;frrk:A1,D2,2;'
        parser = Parse(input_line)
        part = parser.parse_bom_line()
        self.assertIsNone(part)

    def test_format_outputter(self):
        """
        Test the formatted output of multiple lines with some mangled data.
        Additionally, tests that in a tie between 2 MPNs of N occurrences,
        the one with more ReferenceDesignators will be selected.
        """
        bom_lines = [
        'Wintermute Systems -- CASE-19201:A2,A3',
        'AXXX-1000:Panasonic:D1,D8,D9',
        'Z1,Z3;40001;Keystone',
        'Z1,Z3,Z8;40001;Keystone',
        'D1,33,Xr--LOL;BadData-'
        'Wintermute System --- CASE-19201:A5,Z1',
        'Wintermute Systems -- CASE-19201:A7,Z1']

        parts = [Parse(line).parse_bom_line() for line in bom_lines]

        # remove failed parses or parses resulting in None
        parts = [part for part in parts if part] 

        formatted_output = Parse.custom_part_formatter(part_list=parts, record_count=5)
        
        self.assertEqual(formatted_output[0]['Manufacturer'], 'Wintermute Systems')
        self.assertEqual(formatted_output[0]['NumOccurences'], 2)
        self.assertEqual(len(formatted_output[0]['ReferenceDesignators']), 4)

if __name__ == '__main__':
    unittest.main()