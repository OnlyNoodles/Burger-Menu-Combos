"""06_add_combo_v1.
Simple code for the adding combo function as this is the first version.
Modified the menu so that each item is in a category in a combo."""

menu = [{"Combo": "Value", "Burger": {"Beef burger": 5.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Cheezy", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Fries": 1.00}, "Drink": {"Fizzy drink": 1.00}},
        {"Combo": "Super", "Burger": {"Cheeseburger": 6.69},
         "Fries": {"Large fries": 2.00}, "Drink": {"Smoothie": 2.00}}]

new_combo = {}
new_combo["Combo"] = input("Enter combo name: ")
new_combo["Burger"] = {}
new_combo["Burger"][input("Enter burger: ")] = float(input("Enter burger price: $"))
new_combo["Fries"] = {}
new_combo["Fries"][input("Enter size of fries: ")] = float(input("Enter fries price: $"))
new_combo["Drink"] = {}
new_combo["Drink"][input("Enter drink: ")] = float(input("Enter drink price: $"))

menu.append(new_combo)
print("Combo added successfully.")
print(new_combo)
