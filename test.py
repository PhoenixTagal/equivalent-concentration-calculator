from chemical_waste import ChemicalWaste

# test obj
guanidine = ChemicalWaste(name='guanine', type_of_tox_test='ld50 oral', tox_test_result=282,
                       percent_composition=95)

triton = ChemicalWaste(name='triton', type_of_tox_test='ld50 oral', tox_test_result=1900,
                       percent_composition=24)

etoh = ChemicalWaste('etoh', 'lc50 inh', 117, 100)

print(guanidine.designate_waste())
print(' ')
print(triton.designate_waste())
print(' ')
print(etoh.designate_waste())
