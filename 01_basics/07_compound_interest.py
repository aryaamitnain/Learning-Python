p = int(input("Enter Principal Amount : "))
r = int(input("Enter Rate of Interest : "))
t = int(input("Enter Time in Years : "))

ci = p*((1+r/100)**t)

print(f"Compound Interest is {ci}.")