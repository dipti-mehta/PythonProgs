def fun_prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i ==0 or i == 1:
            continue
        else:
            for j in range(x, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = 2
ending_range = 7
lst = fun_prime(starting_range, ending_range)
if len(lst) == 0:
    print("no prime nos in given range")
else:
    print("prime nos are", lst)

# -----gfg flag method--------------------------------
# Python program to print all
# prime number in an interval

def prime(starting_range, ending_range):
    lst = []
    flag = 0  # Declaring flag variable
    # elements range between starting and ending range
    for i in range(starting_range, ending_range):
        for j in range(2, i):
            if(i % j == 0):  # checking if number is divisible or not
                flag = 1  # if number is divisible, then flag variable will become 1
                break
            else:
                flag = 0
        if(flag == 0):  # if flag variable is 0, then element will append in list
            lst.append(i)
    return lst


# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
