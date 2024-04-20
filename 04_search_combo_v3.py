"""04_search_combo_v3.
Put 04_search_combo_v2 into a while loop so that
it repeatedly asks the user for input. Also added an option to break this loop
in case the user wants to go back."""

import easygui

menu = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
            "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
            "Super": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}

while True:
    # Ask the user for what combo they want to search
    combo_search = easygui.enterbox("\nType the name of the combo you want "
                                    "to search for (use capitals where necessary). "
                                    "To go back to the options menu, enter 'X': ")

    # Search for the combo in the menu
    search_combo = menu.get(combo_search)

    # If the combo is found, print the combo name and what is included
    if search_combo:
        easygui.msgbox(f"\nCombo: {combo_search}")
        for item, price in search_combo.items():
            easygui.msgbox(f"{item}: ${price}")

    elif combo_search == "X":
        break

    else:
        easygui.msgbox("\nPlease enter a valid combo.")

