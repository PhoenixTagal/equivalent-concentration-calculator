from tox_eval_criteria import valid_tox_test, valid_percent_composition, tox_class_magnitude


class ChemicalWaste:

    def __init__(self, name, type_of_tox_test, tox_test_result, percent_composition):
        """Construct ChemicalWaste object"""
        self.name = name
        self.type_of_tox_test = type_of_tox_test
        # if self.type_of_tox_test not in valid_tox_test.keys():
        #     raise TypeError(f'must input one of the following: {valid_tox_test.keys()}')
        self.tox_test_result = tox_test_result
        self.percent_composition = percent_composition
        # if self.percent_composition not in valid_percent_composition:
        #     raise TypeError('must input an integer between 0 - 100')

    def equivalent_concentration(self):
        """Return equivalent concentration of chemical waste object by determining the correct list of
        thresholds by using referencing the value associated with the type of tox test provided. """
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
            tox_magnitude = 1000000000

        eq_concentration = self.percent_composition / tox_magnitude
        return eq_concentration

    def designate_waste(self):
        """Return WA state toxicity designation"""
        if self.equivalent_concentration() >= 1:
            return f'Chemical Waste: {self.name} \nDesignation: EHW \nWaste code: WT01 \nEquivalent Concentration: {self.equivalent_concentration()}%'
        elif self.equivalent_concentration() >= 0.001:
            return f'Chemical Waste: {self.name} \nDesignation: DW \nWaste code: WT02 \nEquivalent Concentration: {self.equivalent_concentration()}%'
        elif self.equivalent_concentration() < 0.001:
            return f'Chemical Waste: {self.name} \nDoes not designate as \ndangerous waste at this concentration'






