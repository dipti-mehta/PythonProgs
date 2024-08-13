class Computer:  # defining a class

    def config(self):  # defining a method, self is the object that we are passing
        print("i5, 16gb, 1Tb")


com1 = Computer()  # object of class computer
com2 = Computer()

Computer.config(com1) # i want the config for user/object com1

# alternate way for line 10
com1.config()
com2.config()