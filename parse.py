import json
from part import Part

class Parse():
    def __init__(self, input_line):
        self.input_line = input_line
        return
    
    def handle_f1(self):
        """
        Format 1
        MPN:Manufacturer:ReferenceDesignators
        TSR-1002:Panasonic:A1,D2
        """
        bom_info = self.input_line.split(':')

        if not len(bom_info) == 3:
            return None

        part = Part(
            mpn = bom_info[0],
            manufacturer = bom_info[1],
            reference_designators = bom_info[2])

        return part
    
    def handle_f2(self):
        """
        Format 2
        Manufacturer -- MPN:ReferenceDesignators
        Panasonic -- TSR-1002:A1
        """
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
        """
        Format 3
        ReferenceDesignators;MPN;Manufacturer
        """
        bom_info = self.input_line.split(';')
        
        if not len(bom_info) == 3:
            return None

        part = Part(
            mpn = bom_info[1], 
            reference_designators = bom_info[0],
            manufacturer = bom_info[2])
        
        return part

    def parse_bom_line(self):
        """
        Do some basic checks on what we expect to happen when we split a bomline.
        If none of the check conditions pass, then we will return None.
        Do this to avoid issues with manufacturer name containing a split char.
        """
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

    @staticmethod
    def custom_part_formatter(part_list, record_count):
        """
        Requires a list of Part Objects and Returns custom json output.
        Requires list of records to return.
        """
        
        formatted_parts = []
        part_group_keys = list(set([part.part_key for part in part_list]))

        for part_key in part_group_keys:
            count = 0
            reference_designator_all = []
            for part in part_list:
                if part_key == part.part_key:
                    count += 1
                    reference_designator_all.extend(part.reference_designators)
                    manufacturer = part.manufacturer
                    mpn = part.mpn

            # remove dupes.
            reference_designator_all = list(set(reference_designator_all))

            new_part = Part(
                mpn = mpn,
                manufacturer = manufacturer,
                reference_designators = reference_designator_all,
                )

            # override the num occurences with current part count
            new_part.num_occurences = count
            formatted_parts.append(new_part)
        
        # sorts the list by num occurences, descending.
        # filters by number of records requested when calling custom_part_formatter()
        newlist = sorted(
            [p.as_dict() for p in formatted_parts], 
            key=lambda k: k['NumOccurences'], 
            reverse=True)[:record_count]

        return newlist