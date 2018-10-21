from parse import Parse
from parse import Part
import argparse

parser = argparse.ArgumentParser(description='Process a BOM.')
parser.add_argument('records', type=int,
                    help='The number of records to print.')

parser.add_argument('--bomfile', type=str,
                    help='Name of the bomfile.')

parser.add_argument('--bomlines', type=str, help='Bom lines pasted to STDIN.')

args = parser.parse_args()

if not args.bomfile and not args.bomlines:
    print('You must provide a bomfile or a set of bomlines to run the program.')
elif args.bomfile and args.bomlines:
    print('Please provide either a bomfile or pasted bomlines.')

if args.bomfile:
    with open(args.bomfile) as file:
        lines = file.readlines()
        parts = [Parse(line.rstrip('\n')).parse_bom_line() for line in lines]

#TODO: fix this so that it flips to read stdin stream until there are two newlines.
elif args.bomlines:
    lines = bomlines.split('\n')
    parts = [Parse(line).parse_bom_line() for line in lines]


part_group_keys = list(set([part.part_key for part in parts]))

pgc = {}
formatted_parts = []
for part_key in part_group_keys:
    #print("Handling {}".format(part_key))
    count = 0
    reference_designator_all = []
    for part in parts:
        if part_key == part.part_key:
            count += 1
            reference_designator_all.extend(part.reference_designators)
            manufacturer = part.manufacturer
            mpn = part.mpn

    # remove dupes.
    reference_designator_all = list(set(reference_designator_all))

    new_part = Part(mpn = mpn,
        manufacturer = manufacturer,
        reference_designators = reference_designator_all,
        )
    pgc[part_key] = count

    # override the num occurences with current part count
    new_part.num_occurences = count
    formatted_parts.append(new_part)


newlist = sorted(
    [p.as_dict() for p in formatted_parts], 
    key=lambda k: k['NumOccurences'], 
    reverse=True)[:args.records]


import json
print(json.dumps(newlist)) 