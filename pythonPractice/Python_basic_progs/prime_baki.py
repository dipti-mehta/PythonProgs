# ------prime number using flag variable------
from math import sqrt
n = 11
flag_no_prime = 0
if n > 1:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            flag_no_prime = 1
            break
    if flag_no_prime == 0:
        print("true")
    else:
        print("false")
else:
    print("false")

# -----prime number using recursion-------
def fun_prime(num1, itr):
    if itr == 1:
        return True
    if num1 % itr == 0:
        return False
    if fun_prime(num1, itr - 1) == False:
        return False

    return True


num1 = 13
itr = int(sqrt(num1) + 1)
prime_num = fun_prime(num1, itr)
