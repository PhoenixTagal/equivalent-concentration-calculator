# create eq conc calculator

from tox_eval_criteria import valid_tox_test, valid_percent_composition, tox_class_magnitude

class ChemicalWaste:
    # name arg must be equal to a key from valid_tox_test dict
    def __init__(self, name, type_of_tox_test, tox_test_result, percent_composition):
        self.name = name
        self.type_of_tox_test = type_of_tox_test
        self.tox_test_result = tox_test_result
        self.percent_composition = percent_composition

    def equivalent_concentration(self):
        pass


hcl = ChemicalWaste(name='hcl', type_of_tox_test='ld50 oral', tox_test_result= 4000,
                    percent_composition=50)

print(valid_tox_test[hcl.type_of_tox_test])


