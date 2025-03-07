# Chemistry & Geometry Calculator 🧪📐

## 📌 Description
This project integrates two calculators:

- **Chemical Calculator**: Calculates the concentrations of chemical solutions.
- **Geometry Calculator**: Calculates areas and volumes of geometric shapes.

The user selects the type of calculator and performs calculations based on a simple menu.

## 🧪 Chemical Calculation Methods
This project contains methods for converting and calculating different concentration units used in chemistry, specifically for molar concentration (Cm) and percentage concentration (Cp). The formulas used are based on classical chemical principles for converting between these units, as well as methods for mixing solutions and calculating mass ratios.

### Methods

1. **count_Cm_to_Cp(density, molar_mass, Cm)**
   Converts molar concentration (Cm) to percentage concentration (Cp).
   
   - **Cm** = Molar concentration (mol/L)
   - **M** = Molar mass (g/mol)
   - **ρ** = Density (g/cm³)

   **Result:** Returns the percentage concentration (Cp) in **%**.

2. **count_Cp_to_Cm(density, molar_mass, Cp)**
   Converts percentage concentration (Cp) to molar concentration (Cm).
   
   - **Cp** = Percentage concentration (%)
   - **ρ** = Density (g/cm³)
   - **M** = Molar mass (g/mol)

   **Result:** Returns the molar concentration (Cm) in **mol/L**.

3. **count_Cm(volume_of_solution, mass_of_substance, molar_mass)**
   Calculates molar concentration (Cm) from volume, mass of substance, and molar mass.

   - **m** = Mass of the substance (g)
   - **V** = Volume of the solution (L)
   - **M** = Molar mass (g/mol)

   **Result:** Returns molar concentration (Cm) in **mol/L**.

4. **count_mass_ratio_by_cross_method(Cp1, Cp2, Cp_wanted)**
   Calculates the mass ratio by using a cross method based on given concentrations.

   - **Cp1** = Initial percentage concentration (%)
   - **Cp2** = Second percentage concentration (%)
   - **Cp_wanted** = Desired percentage concentration (%)

   **Result:** Returns the mass ratio (no units).

5. **count_Cp_by_mass_ratio(Cp1, Cp2, mass1, mass2)**
   Calculates the resulting concentration (Cp) of a mixture based on the mass and concentration of the two components.
   
   - **Cp1** = Percentage concentration of the first solution (%)
   - **Cp2** = Percentage concentration of the second solution (%)
   - **m1** = Mass of the first component (g)
   - **m2** = Mass of the second component (g)

   **Result:** Returns the resulting percentage concentration (**%**).

## 💻 Technologies
- Python 3.x
- Standard Libraries: math, fractions, enum

## ⚙️ Conclusion
The methods provided in this project allow for accurate calculations of molar and percentage concentrations, as well as mixing ratios and solution preparations. These calculations are widely used in chemistry and can assist in various solution preparation and concentration conversion tasks.
