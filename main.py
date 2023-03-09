# create eq conc calculator


class ChemicalWaste:

    valid_tox_test = ['lc50 inh',
                      'lc50 fish',
                      'ld50 dermal',
                      'ld50 oral']
    
    valid_concentration = list(range(101))

    def __init__(self, name, type_of_tox_test, tox_test_result):
        self.name = name
        self.type_of_tox_test = type_of_tox_test
        self.tox_test_result = tox_test_result

