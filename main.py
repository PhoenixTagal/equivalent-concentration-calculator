"""main.py creates instances of main GUI by creating a EquivalentConcentrationCalculatorGUI object.
.get() from entry fields on GUI are used to create an instance of ChemicalWaste.
ChemicalWaste methods are called on newly constructed instance of ChemicalWaste object and return values are shown in
text window on the EquivalentConcentrationCalculatorGUI object. Calculate button on GUI is tied to calling
ChemicalWaste.designate_waste()"""


import customtkinter
from chemical_waste import *
from tox_eval_criteria import *
from gui_root import *
from tkinter import *


def getinfo():
    waste = ChemicalWaste(name=gui.chemical_name_entry,
                          type_of_tox_test=gui.type_of_tox_test_dropdown,
                          tox_test_result=gui.tox_test_result_entry.get,
                          percent_composition=gui.percent_composition_entry)
    return waste.designate_waste()



# construct instance of GUI
gui = EquivalentConcentrationCalculatorGUI()




# calculate button config
calculate_button = customtkinter.CTkButton(master=gui,
                                                width=220,
                                                height=60,
                                                text='Calculate',
                                                corner_radius=10,
                                           command=lambda: getinfo())
calculate_button.grid(row=8, pady=20)


gui.mainloop()

