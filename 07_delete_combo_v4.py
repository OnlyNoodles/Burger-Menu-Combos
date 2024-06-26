"""07_delete_combo_v4.
Testing 07_delete_combo_v3 in the option's menu which has the other functions."""

import easygui

menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]

def output():
    menu_text = ""
    for combo, item in menu.items():
        menu_text += f"\nCombo name: {combo}\n"
        for key in item:
            menu_text += f"{key}: {item[key]}\n"
    easygui.msgbox(menu_text, "Menu")


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


# Function for adding combo
def add():
    new_combo = {}
    new_combo["Combo"] = easygui.enterbox("Enter combo name: ")
    new_combo["Burger"] = {}
    new_combo["Burger"][easygui.enterbox("Enter burger: ")] = float(easygui.integerbox("Enter burger price: $"))
    new_combo["Fries"] = {}
    new_combo["Fries"][easygui.enterbox("Enter size of fries: ")] = float(easygui.integerbox("Enter fries price: $"))
    new_combo["Drink"] = {}
    new_combo["Drink"][easygui.enterbox("Enter drink: ")] = float(easygui.integerbox("Enter drink price: $"))

    menu.append(new_combo)
    easygui.msgbox("Combo added successfully.")

    # Puts the new combo into one easygui msgbox
    combo_text = f"Combo: {new_combo['Combo']}\n"
    for category, items in new_combo.items():
        if category != "Combo":
            combo_text += f"{category}:\n"
            for item, price in items.items():
                combo_text += f"  - {item}: ${price:.2f}\n"
    easygui.msgbox(combo_text, "New Combo")


def delete():
    menu_text = ""
    for combo in menu:
        menu_text += f"\nCombo name: {combo['Combo']}\n"
        for category, items in combo.items():
            if category != "Combo":
                menu_text += f"{category}:\n"
                for item, price in items.items():
                    menu_text += f"  - {item}: ${price}\n"
    delete_combo = easygui.enterbox(f"Current menu:\n"
          f"{menu_text}\n"
            "Enter the name of the combo you want to delete: ")

    deleted = False
    for i, combo in enumerate(menu):
        if combo["Combo"] == delete_combo:
            del menu[i]
            deleted = True
            break

    if deleted:
        menu_text = ""
        for combo in menu:
            menu_text += f"\nCombo name: {combo['Combo']}\n"
            for category, items in combo.items():
                if category != "Combo":
                    menu_text += f"{category}:\n"
                    for item, price in items.items():
                        menu_text += f"  - {item}: ${price}\n"
        easygui.msgbox(title="Combo deleted.", msg="Current menu:\n"
              f"{menu_text}")
    else:
        easygui.msgbox("\nCombo not found.")


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
                        "To add a combo, enter '3'.\n"
                        "To delete a combo, enter '4'.\n"
                        "To exit, enter '5'.\n"
                       "What do you want to do today?\n"
                       "Enter here: ")
    if choice == 1:
        output()

    elif choice == 2:
        search()

    elif choice == 3:
        add()

    elif choice == 4:
        delete()

    elif choice == 5:
        break

    else:
        easygui.msgbox("\nPlease enter a valid number.")

easygui.msgbox(f"Goodbye, have a great day {name}!")
