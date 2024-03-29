"""GUI for quick use of tox calculator. Designed to be used while
completing the hazardous waste designation form. The results from this calculator can be
used to fill out the associated fields in the designation form. Will be packaged as
a .EXE for end user to download on their own device."""

import customtkinter
from chemical_waste import *

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('GUI/custom_theme.json')


class EquivalentConcentrationCalculatorGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('600x900')
        self.title('Equivalent Concentration Calculator')

        self.grid_rowconfigure(10, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # configuring labels and entry boxes
        # chemical name config
        self.chemical_name_label = customtkinter.CTkLabel(master=self,
                                                          width=360,
                                                          height=40,
                                                          text='Chemical Name:')
        self.chemical_name_label.grid(row=0, pady=10)
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
        self.type_of_tox_test_dropdown = customtkinter.CTkOptionMenu(master=self,
                                                                     width=360,
                                                                     height=40,
                                                                     values=['lc50 inh', 'lc50 fish', 'ld50 dermal',
                                                                             'ld50 oral'], )
        self.type_of_tox_test_dropdown.grid(row=3)

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
                                                                text='Percent Composition of Waste:')
        self.percent_composition_label.grid(row=6, column=0)
        self.percent_composition_entry = customtkinter.CTkEntry(master=self,
                                                                width=360,
                                                                height=40,
                                                                placeholder_text='0 - 100',
                                                                placeholder_text_color='grey')
        self.percent_composition_entry.grid(row=7, column=0)

        # textbox config
        self.results_label = customtkinter.CTkLabel(master=self,
                                                    width=580,
                                                    height=410,
                                                    text='Calculation Results',
                                                    corner_radius=10,
                                                    fg_color='white')
        self.results_label.grid(row=9, pady=20)
