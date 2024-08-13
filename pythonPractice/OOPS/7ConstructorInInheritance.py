'''if you create object of subclass it will first
try to find init of subclass if it is not found
then it will call init of super class'''
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()
        '''here we are using .__init__ to access
        init of parent class
        and when u create object of sub class
        it will call init of sub class first
        but if u have call super then it will first call
        init of super class then call init of sub class'''
        print("in B Init")

    def feature3(self):
        print("Feature 1 working")

    def feature4(self):
        print("Feature 2 working")

# method resolution order
class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")
        '''in this case it will print init of A
        then init of C bcoz of MRO, acc to MRO whoever
        is in left while inheriting we will give it
        priority so here A is in left'''

        def feat(self):
            super.feature2()
            # c1 = C()
            # c1.feat
            # to represent super class we use super
            # method it can also be used to access
            # features of other classes

b1 = B()  # this is object of it will call init of B
'''but what if u want to call init of A
 is it possible? that we create object of 
 b and call init of both A and B
 for doing this we have some special keyword named super
 '''
c1 = C()