def marvelNumber(num):
            # place holder
            val = 0
            count = 0
            if num % 2 == 0:
                while num > val:
                    val += 1 
                    if num % val == 0:
                        count += 1               
                if count % val == 0:
                    return True
            else:
                return False

print(marvelNumber(6)) # the function would return True
print(marvelNumber(8)) # the function would return False
print(marvelNumber(28)) # the function would return True
print(marvelNumber(9)) # should be false
