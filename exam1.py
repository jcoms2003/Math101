def checkCount(num):
    # place holder
    div = 0
    i = 1
    while (div <= num):
        if num % 2 == 0:
            div += 1
        i += 1
    return div

def marvelNumber(num):
    if checkCount(num) 
    
print(marvelNumber(6)) # the function would return True
print(marvelNumber(8)) # the function would return False
print(marvelNumber(28)) # the function would return True
print(marvelNumber(9)) # should be false
