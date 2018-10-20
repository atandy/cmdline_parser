

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
        self.reference_designators = reference_designators
        self.manufacturer = manufacturer
        return

    def as_json(self):
        d = { 
            "MPN": self.mpn,
            "Manufacturer": self.manufacturer,
            "ReferenceDesignators": self.reference_designators
        }

        return json.dumps(d)

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
            parse_result = part.as_json()

        elif len(self.input_line.split('--')) == 2:
            part = self.handle_f2()
            parse_result = part.as_json()
        
        elif len(self.input_line.split(':')) == 3:
            part = self.handle_f1()
            parse_result = part.as_json()

        if not parse_result:
            #TODO: throw an error here for unable to parse line.
            pass
            
        return parse_result:
            
            