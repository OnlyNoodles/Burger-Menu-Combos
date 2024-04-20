"""04_search_combo_v2.
Incorporated easygui into the code."""

import easygui

menu = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
    "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
    "Super": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}

# Ask the user for what combo they want to search
combo_search = easygui.enterbox("\nType the name of the combo you want "
                                "to search for (use capitals where necessary): ")

# Search for the combo in the menu
search_combo = menu.get(combo_search)

# If the combo is found, print the combo name and what is included
if search_combo:
    easygui.msgbox(f"\nCombo: {combo_search}")
    for item, price in search_combo.items():
        easygui.msgbox(f"{item}: ${price}")
else:
    easygui.msgbox("\nPlease enter a valid combo.")
