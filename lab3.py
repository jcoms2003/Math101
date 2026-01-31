def notAFactorial(num): #there are 2 things wrong with this--how do we fix it to make it return the factorial?
    total = 0
    if num < 0:
        num = num * (-1)
    while(num == num):
        if num < 0:
            break
        else:
            total = total * num
  #          num = num * (-1)
    return num
print(notAFactorial(-5))
