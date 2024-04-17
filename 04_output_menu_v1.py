"""04_output_menu_v1.
First version of the 'Output Menu' function.
"""

menu = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Super": {"Cheeseburger": 6.69, "Large fries:": 2.00, "Smoothie": 2.00}}

for combo, item in menu.items():
    print(f"\nCombo name: {combo}")

    for key in item:
        print(f"{key}: {item[key]}")
