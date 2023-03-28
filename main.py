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


def calculate_button_function():
    name = gui.chemical_name_entry.get()
    test_type = gui.type_of_tox_test_dropdown.get()
    result = gui.tox_test_result_entry.get()
    percent = gui.percent_composition_entry.get()

    waste = ChemicalWaste(name=name,
                          type_of_tox_test=test_type,
                          tox_test_result=float(result),
                          percent_composition=float(percent))
    designation = waste.designate_waste()
    print(designation)


# construct instance of GUI
gui = EquivalentConcentrationCalculatorGUI()

calculate_button = customtkinter.CTkButton(master=gui,
                                           width=220,
                                           height=60,
                                           text='Calculate',
                                           corner_radius=10,
                                           command=calculate_button_function)

calculate_button.grid(row=8, pady=20)

gui.mainloop()
