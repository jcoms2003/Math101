import csv 

# input
age = input("Enter Age: ")
name = input("Enter Name: ")
grade = input("Enter Grade: ")
# list with inputs
myList = [age, name, grade]
# File writing
with open("myfile.csv", "a", newline="") as csvfile:
    infoWrite = csv.writer(csvfile)

    infoWrite.writerow(myList)

    
