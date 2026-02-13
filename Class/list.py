from collections import namedtuple

Student = namedtuple("Student", ["name", "major", "age", "year"])

student1 = Student("Alex", "Computer Science", 25, "Softmore")

print(student1)
