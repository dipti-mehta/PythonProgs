class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

'''here B is child class so if there is no show method in B
then in output it will show "in A show" but if we define 
show method class B ka khudka then it will give
priority to its own show method
'''
a1 = B()
a1.show()