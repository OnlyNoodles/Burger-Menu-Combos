"""03_output_menu_v2
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
while True:
    print("---Welcome to Kavin's Fried Chicken---")
    print()
    # Asks for name
    name = input("Please enter your name: ")
    print()
    # Combines welcome message and name
    print(f"Welcome to the Kavin's Fried Chicken, {name}!")

    output()