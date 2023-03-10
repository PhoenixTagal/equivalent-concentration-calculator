from chemical_waste import ChemicalWaste

# test obj
hcl = ChemicalWaste(name='hcl', type_of_tox_test='ld50 oral', tox_test_result=4000,
                    percent_composition=50)

print(hcl.equivalent_concentration())





