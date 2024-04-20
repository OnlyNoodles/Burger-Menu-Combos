"""04_search_combo_v5.
Testing 04_search_combo_v4 with the rest of the program so far by
implementing it in the option's menu."""

import easygui

menu = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Super": {"Cheeseburger": 6.69, "Large fries:": 2.00, "Smoothie": 2.00}}


# Function for outputting the full menu
def output():
    for combo, item in menu.items():
        easygui.msgbox(f"\nCombo name: {combo}")

        for key in item:
            easygui.msgbox(f"{key}: {item[key]}")


# Function for searching combo
def search():
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
