# create eq conc calculator


class ChemicalWaste:
    # str of one of the four tox tests
    valid_tox_test = {'lc50 inh': [(0.02, 0.2), (0.2, 2), (2, 20), (20, 200)],
                      'lc50 fish': [(0.01, 0.1), (0.1, 1), (1, 10), (10, 100)],
                      'ld50 dermal': [(2, 20), (20, 200), (200, 2000), (2000, 20000)],
                      'ld50 oral': [(0.5, 5), (5, 50), (50, 500), (500, 5000)]}

    tox_class_magnitude = {'x': 1,
                           'a': 10,
                           'b': 100,
                           'c': 1000,
                           'd': 10000}

    # percent composition must be an int between 0-100
    valid_percent_composition = list(range(101))

    # name arg must equal to a key from valid_tox_test dict
    def __init__(self, name, type_of_tox_test, tox_test_result, percent_composition):
        self.name = name
        self.type_of_tox_test = type_of_tox_test
        self.tox_test_result = tox_test_result
        self.percent_composition = percent_composition
