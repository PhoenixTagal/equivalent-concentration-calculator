"""GUI for quick use of tox calculator. Designed to be used while
completing the hazardous waste designation form. The results from this calculator can be
used to fill out the associated fields in the designation form. Will be packaged as
a .EXE for end user to download on their own device."""

import customtkinter
from chemical_waste import *

customtkinter.set_appearance_mode('light')


class EquivalentConcentrationCalculatorGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('600x1000')
        self.title('Equivalent Concentration Calculator')

        self.grid_rowconfigure(10, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # configuring labels and entry boxes
        # chemical name config
        self.chemical_name_label = customtkinter.CTkLabel(master=self,
                                                          width=360,
                                                          height=40,
                                                          text='Chemical Name:')
        self.chemical_name_label.grid(row=0)
        self.chemical_name_entry = customtkinter.CTkEntry(master=self,
                                                          width=360,
                                                          height=40,
                                                          placeholder_text='Input Chemical Name Here',
                                                          placeholder_text_color='grey')
        self.chemical_name_entry.grid(row=1)

        # type of tox test config
        self.type_of_tox_test_label = customtkinter.CTkLabel(master=self,
                                                          width=360,
                                                          height=40,
                                                          text='Type of Tox Test:')
        self.type_of_tox_test_label.grid(row=2, column=0)
        self.type_of_tox_test_entry = customtkinter.CTkEntry(master=self,
                                                          width=360,
                                                          height=40,
                                                          placeholder_text='Choose Tox Test from Drop Down',
                                                          placeholder_text_color='grey')
        self.type_of_tox_test_entry.grid(row=3)

        # tox test result config
        self.tox_test_result_label = customtkinter.CTkLabel(master=self,
                                                          width=360,
                                                          height=40,
                                                          text='Tox Test Result:')
        self.tox_test_result_label.grid(row=4, column=0)
        self.tox_test_result_entry = customtkinter.CTkEntry(master=self,
                                                          width=360,
                                                          height=40,
                                                          placeholder_text='0 - 20,000',
                                                          placeholder_text_color='grey')
        self.tox_test_result_entry.grid(row=5, column=0)

        # percent composition config
        self.percent_composition_label = customtkinter.CTkLabel(master=self,
                                                          width=360,
                                                          height=40,
                                                          text='Percent Composition of Waste')
        self.percent_composition_label.grid(row=6, column=0)
        self.percent_composition_entry = customtkinter.CTkEntry(master=self,
                                                          width=360,
                                                          height=40,
                                                          placeholder_text='0 - 100',
                                                          placeholder_text_color='grey')
        self.percent_composition_entry.grid(row=7, column=0)

        # calculate button config
        self.calculate_button = customtkinter.CTkButton(master=self,
                                                        width=220,
                                                        height=60,
                                                        text='Calculate',
                                                        corner_radius=10,)
        self.calculate_button.grid(row=8)



app = EquivalentConcentrationCalculatorGUI()
app.mainloop()
