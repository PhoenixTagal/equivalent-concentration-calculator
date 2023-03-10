from chemical_waste import ChemicalWaste
from tox_eval_criteria import valid_tox_test, valid_percent_composition, tox_class_magnitude

# test obj
hcl = ChemicalWaste(name='hcl', type_of_tox_test='ld50 oral', tox_test_result=4000,
                    percent_composition=50)

data = hcl.equivalent_concentration()

criteria = []
for thresh_holds in data:
    criteria.append(thresh_holds)

tox_cat = {'x': criteria[0][0],
           'a': criteria[0],
           'b': criteria[1],
           'c': criteria[2],
           'd': criteria[3],
           'non-tox': criteria[3][1]}

if hcl.tox_test_result > tox_cat['non-tox']:
    tox_magnitude = tox_class_magnitude['d']
elif hcl.tox_test_result
