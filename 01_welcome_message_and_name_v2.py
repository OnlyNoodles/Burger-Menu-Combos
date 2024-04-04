"""01_welcome_message_and_name_v2.
This is the first part of the Burger Menu Combos.
It is what the user will see first as soon as they run the program.
I have imported easygui into here as that is what my program will be using."""

import easygui

# Welcome Message
easygui.msgbox("---Welcome to Kavin's Fried Chicken---")
# Asks for name
name = easygui.enterbox("Please enter your name: ")
# Combines welcome message and name
easygui.msgbox(f"Welcome to the Kavin's Fried Chicken, {name}!")
