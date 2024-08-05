# kalkulator liczący rozcieńczenia.

from enum import Enum, auto
from enum import IntEnum
from pprint import pprint
from fractions import Fraction
from validation import *


# klasa podklasy Enum(wykorzystuje moduł enum)


class Menu_Concentration(Enum):
    Cm_to_Cp = auto()
    Cp_to_Cm = auto()
    Cp = auto()
    Count_Cpx = auto()
    Count_Mass_Ratio = auto()


class ConcentrationCalculator:
    """to do chemical calculations with concentrations
    """

    def count_Cm_to_Cp(self, density, molar_mass, Cm):
        self.density = density
        self.molar_mass = molar_mass
        self.Cm = Cm
        return (self.Cm * self.molar_mass * 100) / self.density

    def count_Cp_to_Cm(self, density, molar_mass, Cp):
        self.density = density
        self.molar_mass = molar_mass
        self.Cp = Cp
        return (self.Cp * self.density) / (100 * self.molar_mass)

    def count_Cm(self, volume_of_solution, mass_of_substance, molar_mass):
        """count mole concentration from mass substance and solution volume
        """
        self.volume_of_solution = volume_of_solution
        self.mass_of_substance = mass_of_substance
        self.molar_mass = molar_mass
        return (mass_of_substance / molar_mass) / volume_of_solution

    def count_mass_ratio_by_cross_method(self, Cp1_key, Cp2_key, Cp_you_want):
        """
          you can calculate the mass ratio. That is, how many [g] 
          of the substance of concentration Cp1 and the 
          substance of Cp1 to mix to get your concentration  
        """
        self.Cp1 = Cp1_key
        self.Cp2 = Cp2_key
        self.Cp_you_want = Cp_you_want
        return ((self.Cp2 - self.Cp_you_want) / (self.Cp_you_want - self.Cp1))

    def count_Cp_by_mass_ratio(self, Cp1_key, Cp2_key, solution_mass_1_value, solution_mass_2_value):
        """method allows count Cpx when you know mass of substances (on a lab scale) ms1 and ms2
          and their percent concentration Cp1 and Cp2.
        """
        self.Cp1 = Cp1_key  # Cp1 > Cp2 !
        self.Cp2 = Cp2_key
        self.solution_mass_1 = solution_mass_1_value
        self.solution_mass_2 = solution_mass_2_value

        return (
            ((self.solution_mass_1 * self.Cp1) +
             (self.solution_mass_2 * self.Cp2)) / (self.solution_mass_1 + self.solution_mass_2))


def main():
    print("This is chemical calculator")
    validator = Data_validation()
    while True:
        print(
            """
        Enter what type of operation you want to do.
        (Press number 1-6)
        1. convert  Molar concentration Cm --> percentage concentration Cp.
        2. convert Percentage concentration Cp --> Molar concentration Cm.
        3. Count molar concentration (from mass substance, volume)
        4. calculate percentage concentration when mix two solutions Cpx (the same substance).
        5. Calculate mass ratio (data: Cp1 and Cp2 and Cp you want) when mix two solutions (the same substance)
        6. Exit
        """)
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            density, molar_mass, Cm = validator.data_validation_for_choice_1()
            concentrate = ConcentrationCalculator()
            Cp = concentrate.count_Cm_to_Cp(density, molar_mass, Cm)
            print(f"percentage concentration = {round(Cp, 4)} %")

        elif choice == "2":
            density, molar_mass, Cp = validator.data_validation_for_choice_2()
            concentrate = ConcentrationCalculator()
            Cm = concentrate.count_Cp_to_Cm(density, molar_mass, Cp)
            print(f"molar concentration = {round(Cm, 4)} mol/dm3")

        elif choice == "3":
            volume_of_solution, mass_of_substance, molar_mass \
                = validator.data_validation_for_choice_3()
            concentrate = ConcentrationCalculator()
            Cm = concentrate.count_Cm(
                volume_of_solution, mass_of_substance, molar_mass)
            print(f"molar concentration is {round(Cm, 4)} mol/dm3")

        elif choice == "4":
            while True:
                Cp1_key, solution_mass_1_value, \
                    Cp2_key, solution_mass_2_value \
                    = validator.data_validation_for_choice_4()
                if (Cp1_key > Cp2_key):
                    print("correct data")
                    solution_data_dictionary = {}
                    solution_data_dictionary[Cp1_key] = solution_mass_1_value
                    solution_data_dictionary[Cp2_key] = solution_mass_2_value
                    for i, (Cp_key, solution_mass_value) \
                            in enumerate(solution_data_dictionary.items(), start=1):
                        print(
                            f'Solution {i} data: --> Concentration: {Cp_key}, \
                                  Mass: {solution_mass_value}')

                concentrate = ConcentrationCalculator()
                Cpx = concentrate.count_Cp_by_mass_ratio(
                    Cp1_key, Cp2_key, solution_mass_1_value, solution_mass_2_value)

                print(
                    f"The percentage concentration after mixing the two solutions \
                      is: {round(Cpx, 4)}")

        elif choice == "5":
            Cp1_key, Cp2_key, Cp_you_want, mass_you_want \
                = validator.data_validation_for_choice_5()
            solution_data_list = [Cp1_key, Cp2_key]

            for i, Cp in enumerate(solution_data_list, start=1):
                print(
                    f'Solution {i} data: --> Concentration: {Cp} %')
                print(f'You want to prepare {Cp_you_want} % solution')

            concentrate = ConcentrationCalculator()
            result = concentrate.count_mass_ratio_by_cross_method(
                Cp1_key, Cp2_key, Cp_you_want)
            mass_ratio = Fraction(result).limit_denominator()
            weight_of_one_part = mass_you_want / \
                (mass_ratio.denominator + mass_ratio.numerator)
            mass_of_first_substance = weight_of_one_part * mass_ratio.numerator
            mass_of_second_substance = weight_of_one_part * mass_ratio.denominator
            print(
                f"""to prepare {mass_you_want}g, {Cp_you_want} % solution: the mass ratio is {mass_ratio};
                Use solution1: {round(mass_of_first_substance, 4)} g
                Use solution2: {round(mass_of_second_substance, 4)} g """)

        elif choice == "6":
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2 or 3 ")


if __name__ == "__main__":
    main()


