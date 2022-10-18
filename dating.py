#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 18, 2022
# A dating game program for a Grandparent
# That will decide if you are the right age
# To date their grandchildren.


def main():

    # Spacer
    print("")
    print("This is a dating program for my Grandchildren")
    user_input_age = input("Please enter your age: (1-100): ")

    # Spacer
    print("")
    # Try catch statement
    try:
        # This checks if you are within the right age group to date
        user_input_age = int(user_input_age)
        if user_input_age <= 40 and user_input_age >= 25:
            print("Congrats, you are the right age to date my grandchildren")
        # Outcome message if you fail the age requirements
        else:
            print("Sorry, you are not the right age to date my grandchildren")
        # This is a fail catcher to prevent invalid inputs causing a crash
    except Exception:
        print("Please ONLY enter a NUMBER from 1-100")
        # A final message at the end
    finally:
        print("Thank you for trying this program and my grandchildren!")


if "__main__" == __name__:
    main()
