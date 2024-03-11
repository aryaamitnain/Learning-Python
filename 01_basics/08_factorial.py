# Get user input
num = int(input("Enter any number: "))

# Initializing variables
original_number = num
factorial = 1

# Check if the number is negative, positive or zero 
if num < 0:
    print("Sorry the factorial of negative numbers does not exist.")
elif num == 0:
    print("the factorial of 0 is 1.")
else: # Calculating factorial using a loop
    while num > 1:
        factorial = factorial * num
        num = num - 1
    print(f"Original number is {original_number}")
    print(f"Factorial of {original_number} is {factorial}")
