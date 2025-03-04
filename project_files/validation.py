class DataValidation:
    @staticmethod
    def get_float_input(prompt, condition=lambda x: x > 0):
        """Pobiera liczbę zmiennoprzecinkową i sprawdza warunek walidacji."""
        while True:
            try:
                value = float(input(prompt))
                if condition(value):
                    return value
                print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def data_validation_for_choice_1(self):
        density = self.get_float_input("Enter the density of the solution [g/dm3]: ")
        molar_mass = self.get_float_input("Enter the molar mass of the substance [g/mol]: ")
        Cm = self.get_float_input("Enter the molar concentration [mol/dm3]: ", lambda x: x >= 0)
        return density, molar_mass, Cm

    def data_validation_for_choice_2(self):
        density = self.get_float_input("Enter the density of the solution [g/dm3]: ")
        molar_mass = self.get_float_input("Enter the molar mass of the substance [g/mol]: ")
        Cp = self.get_float_input("Enter the percentage concentration [%]: ", lambda x: x >= 0)
        return density, molar_mass, Cp

    def data_validation_for_choice_3(self):
        volume_of_solution = self.get_float_input("Enter the volume of solution [dm3]: ")
        mass_of_substance = self.get_float_input("Enter the mass of substance [g]: ", lambda x: x >= 0)
        molar_mass = self.get_float_input("Enter the molar mass of substance [g/mol]: ")
        return volume_of_solution, mass_of_substance, molar_mass

    def data_validation_for_choice_4(self):
        while True:
            Cp1 = self.get_float_input("Enter the percentage concentration of solution 1 (Cp1 > Cp2): ")
            mass1 = self.get_float_input("Enter the mass of solution 1 [g]: ", lambda x: x >= 0)
            Cp2 = self.get_float_input("Enter the percentage concentration of solution 2: ", lambda x: x >= 0)
            mass2 = self.get_float_input("Enter the mass of solution 2 [g]: ", lambda x: x > 0)

            if Cp1 > Cp2:
                return Cp1, mass1, Cp2, mass2
            print("Invalid condition: Cp1 must be greater than Cp2. Try again.")

    def data_validation_for_choice_5(self):
        while True:
            Cp1 = self.get_float_input("Enter the percentage concentration of solution 1 (Cp1 > Cp2): ")
            Cp2 = self.get_float_input("Enter the percentage concentration of solution 2: ", lambda x: x >= 0)
            Cp_wanted = self.get_float_input("Enter the desired percentage concentration (Cp_wanted > Cp2): ")

            if Cp_wanted > Cp2:
                mass_wanted = self.get_float_input(f"Enter the mass [g] of {Cp_wanted}% solution you need: ", lambda x: x > 0)
                return Cp1, Cp2, Cp_wanted, mass_wanted

            print("Invalid condition: Cp_wanted must be greater than Cp2. Try again.")
