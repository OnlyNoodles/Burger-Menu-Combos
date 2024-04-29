"""burger_menu_combos.
This is the program that includes all the final versions of each component,
making this the only version of the base code for my program.
I've also changed the options menu to an easygui.buttonbox
to have the user click which option they want to do rather than
having to go through the hassle of typing in a number and potentially getting it wrong.
Because the user can now no longer get it wrong,
I have also removed the error message from the option's menu.
Also changed the restaurant from 'Kavin's Fried Chicken' to
Kavin's Takeaways since there is no fried chicken on the menu."""

import easygui

# Menu with all the combos
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
                    menu_text += f"  - {item}: ${price}\n"
    easygui.msgbox(msg=menu_text, title="Menu")


# Function for searching for a combo
def search():
    # Ask the user for what combo they want to search
    combo_search = easygui.enterbox(msg="\nType the name of the combo you want "
                                    "to search for (use capitals where necessary): ", title="Search Combo")

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
            easygui.msgbox(msg=combo_text, title="Combo Found")
            break

    if not found:
        easygui.msgbox(msg="\nCombo not found.", title="Combo Not Found")


# Function for adding a combo
def add():
    new_combo = {}
    new_combo["Combo"] = easygui.enterbox(msg="Enter combo name: ", title="Add Combo")
    new_combo["Burger"] = {}
    new_combo["Burger"][easygui.enterbox(msg="Enter burger: ", title="Add Combo")] \
        = float(easygui.integerbox(msg="Enter burger price: $", title="Add Combo"))
    new_combo["Fries"] = {}
    new_combo["Fries"][easygui.enterbox(msg="Enter size of fries: ", title="Add Combo")] \
        = float(easygui.integerbox(msg="Enter fries price: $", title="Add Combo"))
    new_combo["Drink"] = {}
    new_combo["Drink"][easygui.enterbox(msg="Enter drink: ", title="Add Combo")] \
        = float(easygui.integerbox(msg="Enter drink price: $", title="Add Combo"))

    menu.append(new_combo)
    easygui.msgbox(msg="Combo added successfully.", title="Combo added")

    # Puts the new combo into one easygui msgbox
    combo_text = f"Combo: {new_combo['Combo']}\n"
    for category, items in new_combo.items():
        if category != "Combo":
            combo_text += f"{category}:\n"
            for item, price in items.items():
                combo_text += f"  - {item}: ${price:.2f}\n"
    easygui.msgbox(combo_text, "New Combo")


# Function for deleting a combo
def delete():
    menu_text = ""
    for combo in menu:
        menu_text += f"\nCombo name: {combo['Combo']}\n"
        for category, items in combo.items():
            if category != "Combo":
                menu_text += f"{category}:\n"
                for item, price in items.items():
                    menu_text += f"  - {item}: ${price}\n"
    delete_combo = easygui.enterbox(msg=f"Current menu:\n"
                                    f"{menu_text}\n"
                                    "Enter the name of the combo you want to delete: ",
                                    title="Delete Combo")

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
        easygui.msgbox(msg=f"Current menu:\n{menu_text}", title="Combo deleted")
    else:
        easygui.msgbox("\nCombo not found.")


# Main routine


# Welcome Message
easygui.msgbox(msg="---Welcome to Kavin's Takeaways---", title="Welcome!")
# Asks for name
name = easygui.enterbox(msg="Please enter your name: ", title="Enter your name")
# Combines welcome message and name
easygui.msgbox(msg=f"Welcome to the Kavin's Takeaways, {name}!", title=f"Welcome, {name}!")

# Option's Menu
while True:
    option = easygui.buttonbox(msg="To view the existing menu, select 'Full Menu'.\n\n"
                                   "To search for a combo from the existing menu, select 'Search Combo'.\n\n"
                                   "To add a combo to the existing menu, select 'Add Combo'.\n\n"
                                   "To delete a combo from the existing menu, select 'Delete Combo'.\n\n"
                                   "To exit, select 'Exit'.\n\n"
                                   "What do you want to do today?", title="Option's Menu",
                               choices=["Full Menu Print", "Search Combo", "Add Combo", "Delete Combo", "Exit"])

    if option == "Full Menu Print":
        output()

    elif option == "Search Combo":
        search()

    elif option == "Add Combo":
        add()

    elif option == "Delete Combo":
        delete()

    elif option == "Exit":
        break

    else:
        easygui.msgbox("\nPlease enter a valid number.")

# Goodbye Message
easygui.msgbox(msg=f"Goodbye, have a great day {name}!", title="Goodbye!")
