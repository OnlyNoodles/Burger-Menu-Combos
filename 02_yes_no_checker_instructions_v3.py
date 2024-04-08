"""02_yes_no_checker_instructions_v3.
If user does not put in 'yes' or 'no',
program will keep asking for 'yes' or 'no'."""


yes_no = ""
while yes_no != "x":

    # Program asks user if they've played before
    yes_no = input("Have you played this game before?: ").lower()

    # If user answers "yes", "y"
    if yes_no == "yes" or yes_no == "y":
        print("What difficulty do you want to play?: ")
    # If user answers "no", "n"
    elif yes_no == "no" or yes_no == "n":
        # Program shows instructions
        print("Instructions")
    # If user answers something other than yes or no, ask the question again
    else:
        print("Please answer 'yes' or 'no'.")
