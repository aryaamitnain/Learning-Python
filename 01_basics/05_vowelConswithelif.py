sub1 = int(input('Enter Your sub1 Marks : '))
sub2 = int(input('Enter Your sub2 Marks : '))
sub3 = int(input('Enter Your sub3 Marks : '))
sub4 = int(input('Enter Your sub4 Marks : '))
sub5 = int(input('Enter Your sub5 Marks : '))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500)*100

print(f"Your Total Marks is {total}")
print(f'In percent {percentage}%')

print("GRADE")

if(percentage>90):
    print('A')
elif(percentage>80):
    print("B")
elif(percentage>70):
    print("C")
elif(percentage>60):
    print("D")
elif(percentage>50):
    print("E")
else:
    print("FAIL")