class Student:

    name = "Manish"
    age = 23
    

    @staticmethod
    def display():
        print(Student.name)
        print(Student.age)

    @staticmethod
    def setAge():
        Student.age += 1

Student.display()
Student.setAge()
Student.display()