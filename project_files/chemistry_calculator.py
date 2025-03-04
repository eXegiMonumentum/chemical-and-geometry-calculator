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
        return (Cm * molar_mass * 100) / density

    @staticmethod
    def count_Cp_to_Cm(density, molar_mass, Cp):
        return (Cp * density) / (100 * molar_mass)

    @staticmethod
    def count_Cm(volume_of_solution, mass_of_substance, molar_mass):
        return (mass_of_substance / molar_mass) / volume_of_solution

    @staticmethod
    def count_mass_ratio_by_cross_method(Cp1, Cp2, Cp_wanted):
        return (Cp2 - Cp_wanted) / (Cp_wanted - Cp1)

    @staticmethod
    def count_Cp_by_mass_ratio(Cp1, Cp2, mass1, mass2):
        return ((mass1 * Cp1) + (mass2 * Cp2)) / (mass1 + mass2)


def chemistry_calculator():
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
