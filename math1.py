import math as m
def numToHund(num):
    num1 = 0
    if num < 0:
        num *= -1
    while num <= 100:
        num += num1
        num += 1
    return num

#def displayNum():
#x = 0
#while 
print(numToHund(10)) # Testing 
print(numToHund(49)) # Testing
print(numToHund(60)) # Testing
print(numToHund(38)) # Testing

# def even 
