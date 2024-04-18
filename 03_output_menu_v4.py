"""03_output_menu_v4.
Incorporated easygui into the function and main routine.
This is the version I will use for my final full program.
"""

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
