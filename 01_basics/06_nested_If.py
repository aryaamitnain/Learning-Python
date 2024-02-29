name = input("Enter Your Name : ")
salary = int(input("Enter Your Salary : "))

print(f"{name} Your Gross Salary is {salary}.")

if(salary<10000):
    hra = salary*10/100
    da = salary*5/100
    print(f"HRA = {hra}")
    print(f"DA = {da}")
    print(f"{name} Your Net Salary is {salary + hra + da}")
else:
    if(salary<20000):
        hra = salary*15/100
        da = salary*10/100
        print(f"HRA = {hra}")
        print(f"DA = {da}")
        print(f"{name} Your Net Salary is {salary + hra + da}")
    else:
        if(salary<30000):
            hra = salary*20/100
            da = salary*15/100
            print(f"HRA = {hra}")
            print(f"DA = {da}")
            print(f"{name} Your Net Salary is {salary + hra + da}")
        else:
            if(salary<40000):
                hra = salary*25/100
                da = salary*20/100
                print(f"HRA = {hra}")
                print(f"DA = {da}")
                print(f"{name} Your Net Salary is {salary + hra + da}")
            else:
                hra = salary*30/100
                da = salary*25/100
                print(f"HRA = {hra}")
                print(f"DA = {da}")
                print(f"{name} Your Net Salary is {salary + hra + da}")