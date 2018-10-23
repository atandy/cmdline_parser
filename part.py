class Part():
    def __init__(self, mpn, reference_designators, manufacturer):
        self.mpn = mpn
        try:
            self.reference_designators = reference_designators.split(',')
        except AttributeError:
            self.reference_designators = reference_designators
        self.manufacturer = manufacturer.rstrip()
        self.part_key = '{}:{}'.format(self.mpn,self.manufacturer)
        self.num_occurences = 1
        return

    def as_dict(self):
        d = { 
            "MPN": self.mpn,
            "Manufacturer": self.manufacturer,
            "ReferenceDesignators": self.reference_designators,
            "NumOccurences": self.num_occurences
        }
        return d

    def as_json(self):
        return json.dumps(self.as_dict())