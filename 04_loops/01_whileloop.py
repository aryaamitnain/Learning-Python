# i = 1
# while i<=10:
#     print(i, end=" ")
#     i +=1

# +++++++++++++ // Exercise // +++++++++++++

# # get user input
# no1 = int(input("Enter where to start: "))
# no2 = int(input("Enter where to stop: "))

# # create while loop

# while no1 <=no2:
#     print(f"{no1}", end=" ")
#     no1+=1


# ++++++++++++++++++ // exercise 2 print tables // +++++++++++++++++

# get user input
starting = int(input("Enter any number from where to start: "))
ending = int(input("Enter any number to where to stop: "))


while starting <= ending:
    i = 1
    while i<=10:
        print(f"{starting*i}", end=" ")
        i +=1
    print()
    starting +=1 




