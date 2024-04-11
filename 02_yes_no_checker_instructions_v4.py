"""02_yes_no_checker_instructions_v4.
Turned yes_no_checker_instructions_v3 into a function.
Also added a 'break' command to break the 'while' loop
when the user answers 'yes' or 'no'.
Typed out instructions. Imported easygui.
This is the version I will use in the base code."""

import easygui

# Function for 'yes' or 'no' checker
def yes_no(question):
    while True:

        # Ask user if they've played before
        answer = easygui.enterbox(question).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            easygui.enterbox("\nWhat difficulty would you like to play?: ")
            break

        # If they say no, show instructions
        elif answer == "no" or answer == "n":
            easygui.msgbox("\n---Instructions---"
                  "\n\n")
            break
        # Otherwise - show error
        else:
            easygui.msgbox("Please answer 'yes' or 'no'.")
    return ()


# Main routine
show_instructions = easygui.enterbox(yes_no("Have you ordered here before? "
                           "\n(Please answer 'yes' or 'no'): "))
