class Student:
    school = 'telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):   # this is instance method because we
        # are passing self means its value will
        # change with diff objects
        return (self.m1 + self.m2 + self.m3)/3
    # def get_m1(self):  # accessor as it is getting the value
    #     return self.m1
    # def get_m1(self, value): # mutator as it is modifying the value
    #     self.m1 = value

    @classmethod    # we have to use this decorator
    # in order to define class method
    def getSchool(cls): # class method as we r passing cls
        # in args and accessing cls var
        return cls.school
        # print(Student.info())

    @staticmethod
    def info():  # static method
        print("this is a student class")
        # Student.info()


s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)
print(s1.avg())
print(Student.getSchool())
Student.info()

