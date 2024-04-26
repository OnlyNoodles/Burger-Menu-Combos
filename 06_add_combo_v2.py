"""06_add_combo_v2.
Incorporated easygui into 06_add_combo_v3."""

import easygui

menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]

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
easygui.msgbox(new_combo)
