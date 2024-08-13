# factorial using recursion
def factorial_boi(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_boi(num - 1)

num = int(input("Enter number whose factorial u want: "))
print("factorial of num is", factorial_boi(num))

#using iterative approach------------------------------------------
def factorial_iter(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
num = 2
print("factorial of num is: ", factorial_iter(num))

# factorial using ternary operator----------------------------------------
def factorial_tern(n):
    return 1 if (n == 0 or n == 1) else n * factorial_tern(n - 1)

n = 10
print("factorial_tern of", n, "is: ", factorial_tern(n))

