#prompt the user to input their age
age = int(input("Please enter your age: "))

#Compare the user input age with the minimum age required to check eligibility to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

