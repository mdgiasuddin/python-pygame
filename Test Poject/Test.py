class Student:


    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def printStudent(self):
        print(self.name, " ", self.roll)

    def __str__(self):
        return "Name: %s Roll: %s" %(self.name, self.roll)


stdA = Student('Gias Uddin', 10)
print(stdA.name)
print(stdA.roll)

stdA.printStudent()
print(stdA)


