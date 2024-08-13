# find max using if-else----------------------------------------
def maxim_of_two(x, y):
    if x >= y:
        return x
    else:
        return y


num1 = int(input("First number: "))
num2 = int(input("second number: "))

result = maxim_of_two(num1, num2)
print("the max of 2 nos is", result)

# find max using max function---------------------------------------------
a = 1
b = 2
result = max(a, b)
print(result)

# max of 2 nos using ternary operator-------------------------------------
a = 3
b = 4
print(a if a >= b else b)

# max using lambda fun-----------------------------------------------------
something = lambda x, y: x if x > y else y
x = 1
y = 8
res = something(x, y)
print("lambda wala", res)

# using list comprehension-----------------------------------------
a = 1
b = 2
p = [a if a >= b else b]
print("list compre", p)

# using sort method-----------------------------------------------------
a = 2
b = 3
z = [a,b]
print("max is", z[-1])
