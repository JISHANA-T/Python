#STUDENT
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Age: {self.age}")

# Create an object
student1 = Student("Nidhu", "A", "25")
student2 = Student("Roshan", "B","22")
student1.display()
student2.display()

#CONSUMER
class Consumer:
    def __init__(self, name, gender, income):
        self.name = name
        self.gender = gender
        self.income = income

    def display(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Income: {self.income}")

#Create object
consumer1 = Consumer("Anit", "female", "100000")
consumer2 = Consumer("Ashiq", "male", "200000")
consumer3 = Consumer("Anas", "male", "50000")
consumer4 = Consumer("Azhar", "male", "80000")
consumer5 = Consumer("Unni", "male", "150000")

consumer1.display()
consumer2.display()
consumer3.display()
consumer4.display()
consumer5.display()