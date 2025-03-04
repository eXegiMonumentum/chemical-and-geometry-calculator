from chemistry_calculator import chemistry_calculator
from geometry_calculator import geometry_calculator


def main():
    while True:
        print("""
        Choose calculator type:
        1. Geometry calculator
        2. Chemistry calculator
        3. Exit
        """)
        choice = input("Choose (1-3): ")

        if choice == "1":
            geometry_calculator()
        elif choice == "2":
            chemistry_calculator()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
