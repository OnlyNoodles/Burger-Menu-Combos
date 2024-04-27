"""03_output_menu_v5."""

import easygui

menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]


# Function for outputting full menu
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
