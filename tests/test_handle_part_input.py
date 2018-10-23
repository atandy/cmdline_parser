from parse import Parse
import unittest

class TestAdd(unittest.TestCase):
    """
    Test multiple lines of mangled data
    """

    def test_multimangled_data(self):
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
        self.assertIsNone(formatted_output)

if __name__ == '__main__':
    unittest.main()