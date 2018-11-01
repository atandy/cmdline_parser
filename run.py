import json
import argparse
import sys
from parse import Parse


parser = argparse.ArgumentParser(description='Process a BOM.')
parser.add_argument('records', type=int,
                    help='The number of records to print.')

parser.add_argument('--bomfile', type=str,
                    help='Name of the bomfile.')

parser.add_argument('--bomlines', type=str, help='Bom lines pasted to STDIN.')

args = parser.parse_args()

# fail if neither bom types are provided or if both are provided.
if not args.bomfile and not args.bomlines:
    print('You must provide a bomfile or a set of bomlines to run the program.')
    sys.exit()
elif args.bomfile and args.bomlines:    
    print('Please provide either a bomfile or pasted bomlines.')
    sys.exit()

if args.bomfile:
    with open(args.bomfile) as file:
        lines = file.readlines()
        parts = [Parse(line.rstrip('\n')).parse_bom_line() for line in lines]

#TODO: fix this so that it flips to read stdin stream until there are two newlines.
elif args.bomlines:
    pass
    
# remove failed parses or parses resulting in None
part_list = [part for part in parts if part]

formatted_output = Parse.custom_part_formatter(
    part_list=part_list, 
    record_count=args.records)

# TODO: tell user which lines failed to parse
if len(part_list) < len(parts):
    print("\nUnable to parse {} lines from the BOM input.\n" \
        "Those entries were not included in the final formatted output below: \n".format(
        len(parts)-len(part_list)))

print(json.dumps(formatted_output, indent=4, sort_keys=True))