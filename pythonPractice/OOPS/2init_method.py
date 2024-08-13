class Computer:

    def __init__(self,cpu,ram):  #taking cpu and ram from object creation
        ''' we need to assign cpu and ram to objects
        and here self is our object
        currently cpu and ram are not connected with object/self'''
        self.cpu = cpu
        self.ram = ram
    def config(self):
        '''now cpu and ram are not simple vars they are
        object attributes so once after associating them with
        self if we need to access it in some other method
        like this config one then we will call
        them like self.cpu and self.ram just like we
        did in print statement here'''
        print("Config is ", self.cpu, self.ram)

com1 = Computer('i5',16)  #object creation and passing args to init
# this computer() is the constructor
# and it calls the init everytime th object is created
com1.config()