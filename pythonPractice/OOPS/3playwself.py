class Computer:

    def __init__(self):
        #instead of passing args we
        # can define directly also the values to vars
        self.name = "shraddha"
        self.age = 25

    def compare(self,com2):
        if self.age == com2.age:
            return True
        else:
            return False

com1 = Computer()
com2 = Computer()

if com1.compare(com2):
    print("they are same")

# com1.name = "rashi"
print(com1.name)
print(com2.name)
# initially it will print shraddha shraddha
# for both com1 and com2 but after we change
# com1.name it will print rashi shraddha
# as value for com1 object is changed
'''if we want to compare 2 objects we have to
 write separate method for it like we wrote
 compare here where we pass one object as self
 and other as other arg'''
