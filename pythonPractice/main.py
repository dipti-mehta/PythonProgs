# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -------------------------------------------------------------------------------
# ********************************************************************************
# ________________________________________________________________________________

# add 2 numbers using recursion
# define 2 numbers or take user input
# define a function and pas those 2 numbers

def order(x):
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n

k = 12300
print("order is: ", order(k))
