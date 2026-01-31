#print("Hello")
#num1 = input()
#num2 = input()

#def add(num1,num2):
#	num1 = input()
#	num2 = input()
#	print(num1 + num2)
#def subtract(num1,num2):
#	num1 = input()
#	num2 = input()
#	print(num1 - num2)
#def divide(num1,num2):
#	num1 = input()
#	num2 = input()
#	print(num1 / num2)
#def multiply(num1,num2):
#	num1 = input()
#	num2 = input()
#	print(num1 * num2)
#def main():
#	choice = input("Enter m for multipy, s for subtract, a for add, d for divide")
#	if choice == 'm':
#		multiply(num1,num2)
#	elif choice == 'a':
#		add(num1,num2)
#	elif choice == 'd':
#		divide(num1,num2)
#	elif choice == 's':
#		subtract(num1,num2)
#	else:
#		print("error")
#main()

import math
x = 0
while x <= 6:
	x += 1
	num1 = float(input("Enter num: "))
	num2 = float(input("Enter num: "))
	num3 = float(input("Enter num: "))
	print("Enter d for divide, m for module, f for floor, r for area of rectangle, tri for triagle, sh for sphere, or q for quit.")
	select = input()

	if select == "d":
		print(num1 / num2)
	elif select == "m":
		print(num1 % num2)
	elif select == "f":
		print(num1 // num2)
	elif select == 'r':
		print(num1 ** 3)
	elif select == 'tri':
		print(0.5 * (num1 * num2))
	elif select == 'sh':
		sphere = (4 * math.pi) * (num3 ** 2)
		print(f'{sphere:.3f}')
	elif select == 'q':
		break
	else:
		print("Error, enter a string")
