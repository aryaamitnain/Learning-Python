# 1. Write a program to add multiple numbers using lists, split and for loop
# 2. Write a program to exchanging values of two variables

# 1. --------------------

# Get the user input
num = input("Enter any number using + : ").split("+")

# Initialize the variables
sum = 0

# creating a for loop 
for i in num:
    sum = sum + int(i)
    # print the result 
print(sum)


# 2 ----------

# # Get the user input
# x = int(input("Enter A: "))
# y = int(input("Enter B: "))

# # exchanging the values
# x,y = y, x

# # printing the result
# print(f"A = {x}")
# print(f"B = {y}")