class Student:
    school =  "GBSSS"
    __schoolId = "123"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print("Name -",self.name)
        print("Marks -",self.marks)

    def grade(self):
        if self.marks >= 60:
            print("First Grade")
        elif self.marks >= 50:
            print("Second Grade")
        elif self.marks >= 35:
            print("Third Grade")
        else:
            print("Failed!")

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def getSchoolId(self,show):
        if show:
            print(self.__schoolId)
        else:
            print("Consent False")

s1 = Student("Manish",78)
s1.display()
s1.grade()
print(s1.school)
s1.getSchoolId(True)