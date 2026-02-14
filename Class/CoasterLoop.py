#Step 0
#input: num -- an int
#output: lst -- a list of ints from 0 to num-1
def basicLoop(num):
    lst = []
    for i in range(num):
        lst.append(i)
    return lst


#Step 1
#input: customers -- the number of customers in line for the ride
#output: lst -- a list full of the numbers from 0 to customers-1 and the string "now that's a line!"
def lineManage(customers):
    lst = []
    for i in range(customers):
        lst.append(i)
    lst.append("now that's a line!")
    return lst 


#Step 2
#input: customers -- the number of customers in line for the ride
#output: lst -- a list full of the numbers from 0 to customers-1, with the splashed customers replaced by "splashed!"
def lineSplash(customers):
    lst = []
    for i in range(customers):
        lst.append(i)
    for i in lst:
        if i % 3 == 0:
            lst[i] = "splashed!"
   
    return lst


#Step 3
#input: num -- some starting int number
#output: lst -- a list from num to 1 and the string "Happy New Years!"
def connieCountdown(num):
    lst = []
    for i in range(num, 0, -1):
        lst.append(i)
    lst.append("Happy New Years!")
    return lst


#Step 4
#input: rolls -- a list of the player's rolls. success -- a list of Connie's rolls
#output: any time one of player's rolls matches one of Connie's, append to lst "Success for [number]"
def ringToss(rolls, success):
    lst = []
    for i in rolls:
       for j in success:
           if i == j:
               lst.append("Success for {}".format(i))
    return lst


#Step 5
#input: start -- random starting number numMoves -- the number of moves that should go into the dance list
#output: dance -- a list full of dance moves based on numMoves and start
def dinerDance(start, numMoves):
    dance = []
    num = int(((start * 2) + 4) / 3)
    for i in range(numMoves):
        num = int(((start * 2) + 4) / 3)
        if num % 3 == 0:
            dance.append("spin")
        elif num % 4 == 0:
            dance.append("side step")
        elif num % 5 == 0:
            dance.append("shake hips")
        elif num % 2 == 0:
            dance.append("freestyle")
        else:
            dance.append("hop")
            
        start = num
    return dance


def main():
    print("Basic Loop returns: {}".format(basicLoop(3)))
    return

if __name__ == "__main__":
    main()

