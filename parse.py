import json
from part import Part

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

        if not len(bom_info) == 3:
            return None

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
        
        if not (len(bom_info) == 2 and len(mpn_rd) == 2):
            return None

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
        
        if not len(bom_info) == 3:
            return None

        part = Part(
            mpn = bom_info[1], 
            reference_designators = bom_info[0],
            manufacturer = bom_info[2])
        
        return part

    def parse_bom_line(self):
        '''
        Do some basic checks on what we expect to happen when we split a bomline.
        If none of the check conditions pass, then we will return None.
        Do this to avoid issues with manufacturer name containing a split char.
        '''
        part = None

        import pdb
        
        
        if len(self.input_line.split(';')) == 3:
            part = self.handle_f3()

        elif part is None and len(self.input_line.split('--')) == 2:
            part = self.handle_f2()
        
        elif part is None and len(self.input_line.split(':')) == 3:
            part = self.handle_f1()
        
        if not part:
            #TODO: throw an error here for unable to parse line.
            pass
        return part