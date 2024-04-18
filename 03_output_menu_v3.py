"""04_output_menu_v3.
Edited the code so that the program asks what the user wants to do.
I will continue to edit the while loop by adding more components as I go.
"""

menu = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Super": {"Cheeseburger": 6.69, "Large fries:": 2.00, "Smoothie": 2.00}}


# Function for outputting the full menu
def output():
    for combo, item in menu.items():
        print(f"\nCombo name: {combo}")

        for key in item:
            print(f"{key}: {item[key]}")


# Main Routine
print("---Welcome to Kavin's Fried Chicken---")
print()
# Asks for name
name = input("Please enter your name: ")
print()
# Combines welcome message and name
print(f"Welcome to the Kavin's Fried Chicken, {name}!")

while True:
    choice = int(input("\nFor a full list print, enter '1'.\n"
                       "To exit, enter '2'.\n"
                       "What do you want to do today?\n"
                       "Enter here: "))
    if choice == 1:
        output()

    elif choice == 2:
        break

    else:
        print("\nPlease enter a valid number.")

print(f"Goodbye, have a great day {name}!")
