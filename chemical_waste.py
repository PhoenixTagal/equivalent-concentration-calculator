from tox_eval_criteria import valid_tox_test, valid_percent_composition, tox_class_magnitude


class ChemicalWaste:
    # type_of_tox_test arg must be equal to a key from valid_tox_test dict
    def __init__(self, name, type_of_tox_test, tox_test_result, percent_composition):
        self.name = name
        self.type_of_tox_test = type_of_tox_test
        if self.type_of_tox_test not in valid_tox_test.keys():
            raise TypeError(f'must input one of the following: {valid_tox_test.keys()}')
        self.tox_test_result = tox_test_result
        self.percent_composition = percent_composition
        if self.percent_composition not in valid_percent_composition:
            raise TypeError('must input an integer between 0 - 100')

    def equivalent_concentration(self):
        evaluation_list = valid_tox_test[self.type_of_tox_test]
        criteria = []
        for thresh_holds in evaluation_list:
            criteria.append(thresh_holds)

        tox_cat = {'x': criteria[0][0],
                   'a': criteria[0][1],
                   'b-lo': criteria[1][0],
                   'b-hi': criteria[1][1],
                   'c-lo': criteria[2][0],
                   'c-hi': criteria[2][1],
                   'd': criteria[3][0],
                   'non-tox': criteria[3][1]}

        if self.tox_test_result < tox_cat['x']:
            tox_magnitude = tox_class_magnitude['x']
        elif self.tox_test_result <= tox_cat['a']:
            tox_magnitude = tox_class_magnitude['a']
        elif self.tox_test_result <= tox_cat['b-hi']:
            tox_magnitude = tox_class_magnitude['b']
        elif self.tox_test_result <= tox_cat['c-hi']:
            tox_magnitude = tox_class_magnitude['c']
        elif self.tox_test_result <= tox_cat['non-tox']:
            tox_magnitude = tox_class_magnitude['d']
        elif self.tox_test_result > tox_cat['non-tox']:
            print(f'{self.name} at this percent is not considered hazardous waste')

        eq_concentration = self.percent_composition / tox_magnitude
        return eq_concentration

            