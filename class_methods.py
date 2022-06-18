class Student:
    schoolName = "GBSSS"
    schoolLevel = 4

    @classmethod
    def display(cls):
        print("School Name - ",cls.schoolName)
        print("School Level - ",cls.schoolLevel)

    @classmethod
    def setLevel(cls,level):
        cls.schoolLevel = level
        print("School level set to {}".format(level))

Student.display()
Student.setLevel(2)
Student.display()

print("**************************************************")
s1 = Student()
s1.display()