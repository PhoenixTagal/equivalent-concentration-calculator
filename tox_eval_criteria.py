"""Criteria for calculations in ChemicalWaste methods"""
valid_tox_test = {'lc50 inh': [(0.02, 0.2), (0.2, 2), (2, 20), (20, 200)],
                  'lc50 fish': [(0.01, 0.1), (0.1, 1), (1, 10), (10, 100)],
                  'ld50 dermal': [(2, 20), (20, 200), (200, 2000), (2000, 20000)],
                  'ld50 oral': [(0.5, 5), (5, 50), (50, 500), (500, 5000)]}

tox_class_magnitude = {'x': 1,
                       'a': 10,
                       'b': 100,
                       'c': 1000,
                       'd': 10000}

valid_percent_composition = list(range(101))