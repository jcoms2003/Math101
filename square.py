import math as m
def square(x):
    myList = []
    seen = set()
    duplicate = set()
    for i in range(0,x):
        num = m.sqrt(i)
        myList.append(num)
    for item in myList:
        if item in seen:
            duplicate.add(item)
        else:
            seen.add(item)
    if len(duplicate) == 0:
        print("All numbers are unique! inverse")
    else:
        print("You have duplicate numbers, not inverse func")
square(5000)
        
