class A:  # parent class/Super class
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    '''B is child class/subclass of class A
    B is inheriting all features of class A
    till this class B it is called single level inheritance'''
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):
    '''now c class can access all features of
    class a,b and c this is called multilevel
    inheritance C-->B-->A
    if B is not child of A and A and B are 2 different classes
    then if c wants properties of both A and B then
    we will use multiple inheritance
    we will define class c as class C(A,B)'''
    def feature5(self):
        print("Feature 5 working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature5()
c1.feature4()
c1.feature3()
c1.feature2()
c1.feature1()
