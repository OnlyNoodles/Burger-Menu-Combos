"""03_output_menu_v4.
Incorporated easygui into the function and main routine.
Also made it so that the full menu is shown in one single easygui box.
This is the version I will use for my final full program.
"""

import easygui

menu = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
        "Super": {"Cheeseburger": 6.69, "Large fries:": 2.00, "Smoothie": 2.00}}


# Function for outputting the full menu
def output():
    menu_text = ""
    for combo, item in menu.items():
        menu_text += f"\nCombo name: {combo}\n"
        for key in item:
            menu_text += f"{key}: {item[key]}\n"
    easygui.msgbox(menu_text, "Menu")

# Main routine

# Welcome Message
easygui.msgbox("---Welcome to Kavin's Fried Chicken---")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Kavin's Fried Chicken, {name}!")

while True:
    choice = easygui.integerbox("\nFor a full list print, enter '1'.\n"
                       "To exit, enter '2'.\n"
                       "What do you want to do today?\n"
                       "Enter here: ")
    if choice == 1:
        output()

    elif choice == 2:
        break

    else:
        easygui.msgbox("\nPlease enter a valid number.")

easygui.msgbox(f"Goodbye, have a great day {name}!")
