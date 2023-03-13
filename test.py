from chemical_waste import ChemicalWaste

# test obj
buffer = ChemicalWaste(name='buffer', type_of_tox_test='lc50 inh', tox_test_result=0.16,
                       percent_composition=3)

print(buffer.designate_waste())