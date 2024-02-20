sub1 = int(input("Enter your Sub1 marks : "))
sub2 = int(input("Enter your Sub2 marks : "))
sub3 = int(input("Enter your Sub3 marks : "))
sub4 = int(input("Enter your Sub4 marks : "))
sub5 = int(input("Enter your Sub5 marks : "))

total = sub1+sub2+sub3+sub4+sub5
percentage = (total/500)*100

print(f"your total marks is {total}.")
print(f"you got {percentage}% ")

if(percentage>50):
    print("PASS")
else:
    print("FAIL")
