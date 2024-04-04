"""02_yes_no_checker_instructions_v1.
Asks if the user has ordered from this restaurant before."""


# Program asks user if they've played before
yes_no = input("Have you ordered at Kavin's Fried Chicken before?: ")

# If user answers "yes", "y", or "Yes"
if yes_no == "yes" or yes_no == "y" or yes_no == "Yes":
    # Ask for game difficulty
    print("Program continues")
# If user answers "no", "n", or "No"
elif yes_no == "no" or yes_no == "n" or yes_no == "No":
    # Program shows instructions
    print("Instructions")
# If user answers something other than yes or no, ask the question again
else:
    print("Please answer 'yes' or 'no'.")
