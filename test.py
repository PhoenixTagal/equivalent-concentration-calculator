from chemical_waste import ChemicalWaste
from tox_eval_criteria import valid_tox_test, valid_percent_composition, tox_class_magnitude

# test obj
hcl = ChemicalWaste(name='hcl', type_of_tox_test='ld50 oral', tox_test_result=4000,
                    percent_composition=50)

data = hcl.equivalent_concentration()

print(data)





