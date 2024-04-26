"""06_add_combo_v3.
Turned 06_add_combo_v2 into a function.
Also added a component to output the new combo into one easygui
msgbox after the user has added their new combo."""

import easygui

menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]

# Function for adding combo
def add():
    new_combo = {}
    new_combo["Combo"] = easygui.enterbox("Enter combo name: ")
    new_combo["Burger"] = {}
    new_combo["Burger"][easygui.enterbox("Enter burger: ")] = float(easygui.enterbox("Enter burger price: $"))
    new_combo["Fries"] = {}
    new_combo["Fries"][easygui.enterbox("Enter size of fries: ")] = float(easygui.enterbox("Enter fries price: $"))
    new_combo["Drink"] = {}
    new_combo["Drink"][easygui.enterbox("Enter drink: ")] = float(easygui.enterbox("Enter drink price: $"))

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


add()
