
class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Course:", self.course)


# Creating objects with different values
s1 = Student("Arijit", 101, "BCA")
s2 = Student("Rahul", 102, "BCA")

s1.display()
print()
s2.display()
