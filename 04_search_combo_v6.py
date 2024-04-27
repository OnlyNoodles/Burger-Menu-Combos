"""04_search_combo_v6.
Changed the search combo function to accommodate for the new menu"""

import easygui

menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]


# Function for outputting the full menu
def output():
    menu_text = ""
    for combo in menu:
        menu_text += f"\nCombo name: {combo['Combo']}\n"
        for category, items in combo.items():
            if category != "Combo":
                menu_text += f"{category}:\n"
                for item, price in items.items():
                    menu_text += f"  - {item}: {price}\n"
    easygui.msgbox(menu_text, "Menu")


# Function for searching combo
def search():
    while True:
        # Ask the user for what combo they want to search
        combo_search = easygui.enterbox("\nType the name of the combo you want "
                                        "to search for (use capitals where necessary). "
                                        "To go back to the options menu, enter 'X': ")

        # If the user wants to go back, break the loop
        if combo_search == "X":
            break

        # Search for the combo in the menu
        found = False
        for combo in menu:
            if combo["Combo"] == combo_search:
                found = True
                combo_text = f"\nCombo: {combo_search}\n"
                for category, items in combo.items():
                    if category != "Combo":
                        for item, price in items.items():
                            combo_text += f"{item}: ${price}\n"
                easygui.msgbox(combo_text)
                break

        if not found:
            easygui.msgbox("\nPlease enter a valid combo.")


# Main routine

# Welcome Message
easygui.msgbox("---Welcome to Kavin's Fried Chicken---")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Kavin's Fried Chicken, {name}!")

while True:
    choice = easygui.integerbox("\nFor a full menu print, enter '1'.\n"
                       "To search for a combo from the menu, enter '2'.\n"
                        "To exit, enter '3'.\n"
                       "What do you want to do today?\n"
                       "Enter here: ")
    if choice == 1:
        output()

    elif choice == 2:
        search()

    elif choice == 3:
        break

    else:
        easygui.msgbox("\nPlease enter a valid number.")

easygui.msgbox(f"Goodbye, have a great day {name}!")
