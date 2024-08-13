# x = 5
# x = 'Navin'
'''When you type x = 5 u get space in memory
which is of type int and when u type x = navin
u get space in ur memory which is of type 
string'''
class Pycharm:
    def execute(self):
        print("compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention Check")
        print("compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()  #myeditor and pycharm both have
# execute method so it doesn't matter if u create
# object for pycharm or myeditor
lap1 = Laptop()
lap1.code(ide)

