# Joshua CS 152 Self Practice
# Trying to work with JSON to have cleaner code
import json
import math as m
# from termcolor import cprint
with open("map.json","r") as f:
    data = json.load(f)

print(data) 

# absolute value | |
def absValue(x,y):
    answer1 = m.fabs(x)
    answer2 = m.fabsy
    return answer1, answer2
# square root 
def sqrRoot(x,y):
    answer1 = m.sqrt(x)
    answer2 = m.sqrt(y)
    return answer1, answer2
# power of
def powerOf(x,y):
    answer1 = m.pow(x,y)
    return answer1
validResponse = ('p','q','a','s')
x = 0
while 0 <= x <= 10:
    x += 1
    select = str(input("Select one of the following:\n'a' for absolute value\n's' for square root\n'p' for power\n'q' for quit\nEnter here: "))
    if select in validResponse:
        if select == 'q':
            break
        else:
            num1 = float(input("Enter a num: "))
            num2 = float(input("Enter another num: "))
            if select == 'a':
                print(absValue(num1,num2))
            elif select == 's':
                print(sqrRoot(num1,num2))
            elif select == 'p':
                print(powerOf(num1,num2))
            # elif select == 'q':
            #     break
            else:
                print("Error")
                # cprint("Error","red")
    else:
        print("Error. Enter a valid choice!")
