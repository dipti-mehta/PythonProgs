# find armstrong number or not with string manipulation
def armstrong(a):
    str_num = str(a)
    order = len(str_num)
    sum = 0
    for digit in str_num:
        sum = sum + (int(digit) ** order)
    if sum == a:
        return "is Armstrong"
    else:
        return "nahi hai"


a = 153
print(armstrong(a))

# find armstrong using ternary operator------------------------------------------------------------


def is_armstrong_number(number):
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number


# Example usage:
num = 153
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
	print(f"{num} is not an Armstrong number")

