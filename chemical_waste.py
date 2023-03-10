from tox_eval_criteria import valid_tox_test, valid_percent_composition, tox_class_magnitude


class ChemicalWaste:
    # type_of_tox_test arg must be equal to a key from valid_tox_test dict
    def __init__(self, name, type_of_tox_test, tox_test_result, percent_composition):
        self.name = name
        self.type_of_tox_test = type_of_tox_test
        self.tox_test_result = tox_test_result
        self.percent_composition = percent_composition

    def equivalent_concentration(self):
        evaluation_list = valid_tox_test[self.type_of_tox_test]
        return evaluation_list

    # def equivalent_concentration(self):
    #     evaluation_list = valid_tox_test[self.type_of_tox_test]
    #     criteria = []
    #     for thresh_holds in evaluation_list:
    #         criteria.append(thresh_holds)
    #
    #     tox_cat = {'x': criteria[0][0],
    #                'a': criteria[0],
    #                'b': criteria[1],
    #                'c': criteria[2],
    #                'd': criteria[3],
    #                'non-tox': criteria[3][1]}
    #
    #     if self.tox_test_result > tox_cat['non-tox']:
    #         tox_magnitude = tox_class_magnitude['d']