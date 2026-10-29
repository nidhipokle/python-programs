class Student:
    def input_data(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll number: "))

    def display_data(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)


student1 = Student()

student1.input_data()
student1.display_data()
