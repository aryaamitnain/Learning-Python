# input from user (Name, Marks, MM) using split method
# Calculate the percentage
# (marks>=85:S), (marks>=75:A), (marks>=65:B), (marks>=55:C), (marks>=50:D), (marks<50:F)
# print student name, percentage, grade
# using only one print function but print all item in a new line

# Get user input
userInput= input("Name, Marks, MM: ").split(",")

# calculate the percentage
per = int(userInput[1])*100/int(userInput[2])

# calculate the grade
if per>=85:
    g = "S"
elif per>=75:
    g = "A"
elif per>=65:
    g = "B"
elif per>=55:
    g = "C"
elif per>=55:
    g = "D"
else:
    g = "F"

# print the result
print(f"Name: {userInput[0]} \nPercentage: {per} % \nGrade: {g}")

