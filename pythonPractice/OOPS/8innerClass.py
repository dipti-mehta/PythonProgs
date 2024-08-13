class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        # lap is the object of Laptop class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    '''consider student also has laptop
    in this case since the laptop will 
    only be used by student so we will
    create a separate laptop class inside
    student class
    laptop class is called inner class'''

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)
    '''laptop class is inside student class
    in order to create object for laptop class 
    it will be created inside the __init__ of
    outer class'''

s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)
print(s1.name, s1.rollno)  # this doesn't look good
# we want that we write s1.show() and it will
# show us all details about s1 student/object
s1.show()
s1.lap.brand
# for different laptop object we can right like
# lap1 = s1.lap
# lap2 = s2.lap