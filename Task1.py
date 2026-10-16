class Student:
    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)
        print("Course:", self.course)
s1 = Student()
s1.name = "Arijit"
s1.roll = 101
s1.course = "BCA"
s2 = Student()
s2.name = "Rahul"
s2.roll = 102
s2.course = "BCA"
print("Student 1 Information:")
s1.display()
print("\nStudent 2 Information:")
s2.display()
