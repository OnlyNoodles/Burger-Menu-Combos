"""02_yes_no_checker_instructions_v2.
Simplifies the code so that whatever capitals are used in the
input question, it will be forced into lowercase."""


# Program asks user if they've played before
yes_no = input("Have you played this game before?: ").lower()

# If user answers "yes", "y"
if yes_no == "yes" or yes_no == "y":
    # Ask for game difficulty
    print("What difficulty do you want to play?: ")
# If user answers "no", "n"
elif yes_no == "no" or yes_no == "n":
    # Program shows instructions
    print("Instructions")
# If user answers something other than yes or no, ask the question again
else:
    print("Please answer 'yes' or 'no'.")
