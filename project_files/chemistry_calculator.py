from fractions import Fraction
from enum import Enum, auto
from validation import DataValidation


class MenuConcentration(Enum):
    CM_TO_CP = auto()
    CP_TO_CM = auto()
    CP = auto()
    COUNT_CPX = auto()
    COUNT_MASS_RATIO = auto()


class ConcentrationCalculator:
    @staticmethod
    def count_Cm_to_Cp(density, molar_mass, Cm):
        """
        Converts molar concentration (Cm) to percentage concentration (Cp).

        :param density: The density of the solution (g/cm³)
        :param molar_mass: The molar mass of the substance (g/mol)
        :param Cm: Molar concentration (mol/L)
        :return: The percentage concentration (Cp) in %
        """
        return (Cm * molar_mass * 100) / density

    @staticmethod
    def count_Cp_to_Cm(density, molar_mass, Cp):
        """
        Converts percentage concentration (Cp) to molar concentration (Cm).

        :param density: The density of the solution (g/cm³)
        :param molar_mass: The molar mass of the substance (g/mol)
        :param Cp: Percentage concentration (g/cm³)
        :return: The molar concentration (Cm) in mol/L
        """
        return (Cp * density) / (100 * molar_mass)

    @staticmethod
    def count_Cm(volume_of_solution, mass_of_substance, molar_mass):
        """
        Calculates molar concentration (Cm) from volume, mass of substance, and molar mass.

        :param volume_of_solution: The volume of the solution (L)
        :param mass_of_substance: The mass of the substance (g)
        :param molar_mass: The molar mass of the substance (g/mol)
        :return: The molar concentration (Cm) in mol/L
        """
        return (mass_of_substance / molar_mass) / volume_of_solution

    @staticmethod
    def count_mass_ratio_by_cross_method(Cp1, Cp2, Cp_wanted):
        """
        Calculates the mass ratio by using a cross method based on given concentrations.

        :param Cp1: Initial percentage concentration (%)
        :param Cp2: Second percentage concentration (%)
        :param Cp_wanted: Desired percentage concentration (%)
        :return: The mass ratio (no units)
        """
        return (Cp2 - Cp_wanted) / (Cp_wanted - Cp1)

    @staticmethod
    def count_Cp_by_mass_ratio(Cp1, Cp2, mass1, mass2):
        """
        calculation of the resulting concentration from mixing
         by mass two solutions of the same substance with different concentrations.

        :param Cp1: Percentage concentration of the first solution (%)
        :param Cp2: Percentage concentration of the second solution (%)
        :param mass1: Mass of the first component (g)
        :param mass2: Mass of the second component (g)
        :return: The resulting concentration (Cp) in %
        """
        return ((mass1 * Cp1) + (mass2 * Cp2)) / (mass1 + mass2)


def chemistry_calculator():
    """
    A menu-driven function that allows the user to perform various chemical calculations.

    The user can choose between converting concentrations, calculating molar concentration,
    or determining mass ratios for mixing solutions.
    """
    validator = DataValidation()
    calculator = ConcentrationCalculator()

    while True:
        print("""
        Choose an operation:
        1. Cm -> Cp
        2. Cp -> Cm
        3. Calculate molar concentration
        4. Calculate Cp after mixing two solutions
        5. Calculate mass ratio
        6. Back to main menu
        """)
        choice = input("Choose (1-6): ")

        try:
            if choice == "1":
                density, molar_mass, Cm = validator.data_validation_for_choice_1()
                print(f"Percentage concentration = {round(calculator.count_Cm_to_Cp(density, molar_mass, Cm), 4)} %")
            elif choice == "2":
                density, molar_mass, Cp = validator.data_validation_for_choice_2()
                print(f"Molar concentration = {round(calculator.count_Cp_to_Cm(density, molar_mass, Cp), 4)} mol/dm3")
            elif choice == "3":
                volume, mass, molar_mass = validator.data_validation_for_choice_3()
                print(f"Molar concentration = {round(calculator.count_Cm(volume, mass, molar_mass), 4)} mol/dm3")
            elif choice == "4":
                Cp1, mass1, Cp2, mass2 = validator.data_validation_for_choice_4()
                print(
                    f"Concentration after mixing = {round(calculator.count_Cp_by_mass_ratio(Cp1, Cp2, mass1, mass2), 4)} %")
            elif choice == "5":
                Cp1, Cp2, Cp_wanted, mass_wanted = validator.data_validation_for_choice_5()
                ratio = Fraction(calculator.count_mass_ratio_by_cross_method(Cp1, Cp2, Cp_wanted)).limit_denominator()
                unit_mass = mass_wanted / (ratio.numerator + ratio.denominator)
                print(f"To prepare a {Cp_wanted}% solution, mix:")
                print(f" - {round(unit_mass * ratio.numerator, 4)} g of {Cp1}% solution")
                print(f" - {round(unit_mass * ratio.denominator, 4)} g of {Cp2}% solution")
            elif choice == "6":
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
