"""GUI for quick use of tox calculator. Designed to be used while
completing the hazardous waste designation form. The results from this calculator can be
used to fill out the associated fields in the designation form. Will be packaged as
a .EXE for end user to download on their own device."""


import customtkinter
from chemical_waste import *


class EquivalentConcentrationCalculatorGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1000x600')
        self.title('Equivalent Concentration Calculator')









app = EquivalentConcentrationCalculatorGUI()
app.mainloop()