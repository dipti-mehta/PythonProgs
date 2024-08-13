# factorial using in built function-----------------
import math
import numpy


def fact_inbuilt(nn):
    return math.factorial(nn)


n = 3
print("factorial of n using in built func is", fact_inbuilt(n))

# factorial using numpy.prod
n = 5
x = numpy.prod([i for i in range(1, n+1)])
print(x)
