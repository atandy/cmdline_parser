

''' 
{
    "MPN": "AXXX-1000",
    "Manufacturer": "Panasonic",
     "ReferenceDesignators": [
     "D1",
     "D8",
     "D9"
    ]
}'''
import json

class Part():
    def __init__(self, mpn, reference_designators, manufacturer):
        self.mpn = mpn
        self.reference_designators = reference_designators.split(',')
        self.manufacturer = manufacturer
        self.part_key = '{}:{}'.format(self.mpn,self.manufacturer)
        return

    def as_dict(self):
        d = { 
            "MPN": self.mpn,
            "Manufacturer": self.manufacturer,
            "ReferenceDesignators": self.reference_designators,
            "PartKey": self.part_key
        }
        return d

    def as_json(self):
        return json.dumps(self.as_dict())

'''
Format 1
MPN:Manufacturer:ReferenceDesignators
TSR-1002:Panasonic:A1,D2





A1,B2,C8;TSR-1002;Keystone
'''

class Parse():
    def __init__(self, input_line):
        self.input_line = input_line
        return
    
    def handle_f1(self):
        '''
        Format 1
        MPN:Manufacturer:ReferenceDesignators
        TSR-1002:Panasonic:A1,D2
        '''
        bom_info = self.input_line.split(':')
        part = Part(
            mpn = bom_info[0],
            manufacturer = bom_info[1],
            reference_designators = bom_info[2])
        return part
    
    def handle_f2(self):
        '''
        Format 2
        Manufacturer -- MPN:ReferenceDesignators
        Panasonic -- TSR-1002:A1
        '''
        bom_info = self.input_line.split('--')
        mpn_rd = bom_info[1].split(':')
        
        part = Part(
            mpn = mpn_rd[0],
            manufacturer = bom_info[0],
            reference_designators = mpn_rd[1])
        
        return part

    def handle_f3(self):
        '''
        Format 3
        ReferenceDesignators;MPN;Manufacturer
        '''
        #mpn, reference_designators, manufacturer
        bom_info = self.input_line.split(';')
        part = Part(
            mpn = bom_info[1], 
            reference_designators = bom_info[0],
            manufacturer = bom_info[2])
        return part

    def parse_bom_line(self):
        '''
        Do some basic checks on what we expect to happen when we split.
        If none of the check conditions pass, then we will return None.
        Do this to avoid issues with manufacturer name containing a split char.
        '''

        parse_result = None

        if len(self.input_line.split(';')) == 3:
            part = self.handle_f3()
            parse_result = part

        elif len(self.input_line.split('--')) == 2:
            part = self.handle_f2()
            parse_result = part
        
        elif len(self.input_line.split(':')) == 3:
            part = self.handle_f1()
            parse_result = part

        if not parse_result:
            #TODO: throw an error here for unable to parse line.
            pass

        return parse_result
      

#- MPN and manufacturer most common
# An MPN can appear on multiple lines. MPNs with different Manufacturers should be treated as different MPN.

# parse all bomlines and get the parts
#TESTING
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



as_list = []
for part in parts:

    group_key = [part.mpn+part.manufacturer]
    as_list.append()

class BOM():
    def __init__(self):
        self.part_list = []
        self.part_keys = []
        part_key_dict = {}
        return

    def add_part(self, part):
        self.part_list.append()

    def count_parts():

        return 

    def thing():
        processed_keys = []
        part_key_dict = {}
        for part in parts:
            if part.part_key in processed_keys:
                # try to append designators 
                part_key_dict[part.part_key] = list(set(part_key_dict[part.part_key]['ReferenceDesignators'].append(part.ReferenceDesignators)))
            else:
                part_key_dict[part.part_key] = part.as_dict()

    def process_bom():
        post_processed_bom = []
        return post_processed_bom
            