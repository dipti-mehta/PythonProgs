# https://www.geeksforgeeks.org/python-program-to-add-two-numbers/
# Using “+” operator#################################################
a = 10
b = 15
sum = a + b
print("Sum of",a, "and", b, "is", sum)

# Defining a function that adds two number############################
def sum_func(c, d):
    e = c + d
    return e
print("addition of c and d is", sum_func(10,3))

#add two numbers with user input######################################

number1 = input("First number: ")
number2 = input("\nSecond number: ")

# User might also enter float numbers
sum = float(number1) + float(number2)

# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))

# Using operator.add method################################################

num1 = 15
num2 = 12

# Adding two nos
import operator
su = operator.add(num1,num2)

# printing values
print("Sum of {0} and {1} is {2}" .format(num1, num2, su))


# Using lambda function####################################################
add_nums = lambda x, y:x+y
n1 = 3
n2 = 8

res = add_nums(n1,n2)
print(res)

# Using Recursive function#################################################

# Define a recursive function to add two numbers
def add_numbers_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x + 1, y - 1)

# Take input from the user
num1 = 1
num2 = 2

# Call the recursive function to add the two numbers
result = add_numbers_recursive(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)
