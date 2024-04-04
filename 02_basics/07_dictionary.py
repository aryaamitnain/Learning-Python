
thisdict = {
    "course" : "Olevel",
    "institute" : "IIHT",
    "result" : "pass",
    "year": 2024,
    "year" : 2023 # duplicate values are not allowed in dictionaries so one will be deleted in result 
}
print(len(thisdict))
print(thisdict)
# print(thisdict["course"])
# print(thisdict.get("institute"))

# for loop in dictionary 

# for i in thisdict:
#     print(i, end=" - ")   # returns the all key of dictionary 
#     print(thisdict[i])  # returns the values from the  dictionary in loop 

# for i in thisdict.items():
#     print(i)

if "course" in thisdict:
    print("yes")
else:
    print("NO")