class Car:

    wheels = 4 # this is class var

    def __init__(self):
        self.mil = 100
        self.com = "BMW"
        '''the upper ones are called instance 
        variables bcoz as the instance/object changes the
        values of these vars also change'''

c1 = Car()
c2 = Car()

Car.wheels = 5

c1.mil = 80
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)