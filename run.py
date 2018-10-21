from parse import Parse
import argparse



parser = argparse.ArgumentParser(description='Process a BOM.')
parser.add_argument('--records', type=int,
                    help='The number of records to print.')

parser.add_argument('--bomfile', type=str,
                    help='Name of the bomfile.')

parser.add_argument('--bomlines', type=str, help='Bom lines pasted to STDIN.')

args = parser.parse_args()

parts = []

with open(args.bomfile) as file:
    lines = file.readlines()

    parts = [Parse(line).parse_bom_line() for line in lines]

print(parts)
'''
as_list = []
for part in parts:

    group_key = [part.mpn+part.manufacturer]
    as_list.append()
'''
'''
bomlines = ['TSR-1002:Panasonic:A1,D2', 'TSR-1002:Panasonic:A1,D2']
parts = [Parse(line).parse_bom_line() for line in bomlines]
#pd.DataFrame([p.as_dict() for p in parts])

parts_list = []
part_group_keys = {}


for part in parts:
    part_dict = part.as_dict()
    # assign a list for the key 
    part_group_keys[part_dict['PartKey']] = []
    part_group_keys[part_dict['PartKey']].append(part_dict)
    # merge reference designators

'''