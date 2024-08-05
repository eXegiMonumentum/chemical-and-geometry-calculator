
class Data_validation:
    def data_validation_for_choice_1(self):
        while True:
            try:
                density = float(
                    input("Enter the density of the solution in [g/dm3]: "))
                molar_mass = float(
                    input("Enter the molar mass of the substance [g/mol]: "))
                Cm = float(
                    input("Enter the molar concentration of substance M [mol/dm3]: "))

                if density > 0 and molar_mass > 0 and Cm >= 0:
                    return density, molar_mass, Cm
                else:
                    print("Enter the positive numbers. ")
            except ValueError:
                print("Enter the correct numbers")

    def data_validation_for_choice_2(self):
        while True:
            try:
                density = float(
                    input("Enter the density of the substance in [g/dm3]: "))
                molar_mass = float(
                    input("Enter the molar mass of the substance: [g/mol]: "))
                Cp = float(
                    input("Enter the percentage concentration of substance [%] "))

                if density > 0 and molar_mass > 0 and Cp >= 0:
                    return density, molar_mass, Cp
                else:
                    print("Enter the positive data values")
            except ValueError:
                print("Enter correct numbers")

    def data_validation_for_choice_3(self):
        while True:
            try:
                volume_of_solution = float(
                    input("Enter the volume of solution [dm3]: "))
                mass_of_substance = float(
                    input("Enter the mass of substance [g]: "))
                molar_mass = float(
                    input("Enter the molar mass of substance [g/mol]: "))
                if volume_of_solution > 0 and mass_of_substance >= 0 and molar_mass > 0:
                    return volume_of_solution, mass_of_substance, molar_mass
                else:
                    print("Enter the positive data values")
            except ValueError:
                print("Enter correct numbers")

    def data_validation_for_choice_4(self):
        while True:
            try:
                Cp1_key = float(
                    input("""Enter the percentage concentration of solution1
                        CONDITION :  Cp1 > Cp2  """))
                solution_mass_1_value = float(
                    input("enter the solution1 mass [g] "))
                Cp2_key = float(
                    input("Enter the percentage concentration of solution2 "))
                solution_mass_2_value = float(
                    input("enter the solution2 mass [g] "))
                if (Cp1_key > Cp2_key):
                    print("Correct data")
                else:
                    print("Invalid condition")
                    continue
                if Cp1_key > 0 and solution_mass_1_value >= 0 and Cp2_key >= 0 and solution_mass_2_value > 0:
                    return Cp1_key, solution_mass_1_value, Cp2_key, solution_mass_2_value
                else:
                    print("Enter the positive data values")

            except ValueError:
                print("Enter correct numbers")

    def data_validation_for_choice_5(self):
        while True:
            try:
                Cp1_key = float(
                    input("""Enter the percentage concentration of solution1
                        CONDITION :  Cp1 > Cp2:  """))
                Cp2_key = float(
                    input("Enter the percentage concentration of solution2: "))
                Cp_you_want = float(
                    input("""Enter the Cp (percentage concentration you want:
                           Cp you want > Cp2 ! """))
                if (Cp_you_want < Cp2_key):
                    print("Invalid condition, enter data again")
                    continue

                mass_you_want = float(
                    input(f"Enter the mass [g] of {Cp_you_want}% solution you need: "))
                if Cp1_key > 0 and Cp2_key >= 0 and Cp_you_want >= 0 and mass_you_want > 0:
                    return Cp1_key, Cp2_key, Cp_you_want, mass_you_want
                else:
                    print("Enter the positive data values")
            except ValueError:
                print("Enter correct numbers")
