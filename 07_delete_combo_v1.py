"""07_delete_combo_v1."""


menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]

menu_text = ""
for combo in menu:
    menu_text += f"\nCombo name: {combo['Combo']}\n"
    for category, items in combo.items():
        if category != "Combo":
            menu_text += f"{category}:\n"
            for item, price in items.items():
                menu_text += f"  - {item}: {price}\n"
print(f"Current menu:\n"
      f"{menu_text}\n\n")

delete_combo = input(f"Enter the name of the combo you want to delete: ")
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
                    menu_text += f"  - {item}: {price}\n"
    print(f"Combo deleted. Current menu:\n"
          f"{menu_text}")
else:
    print("\nCombo not found.")
