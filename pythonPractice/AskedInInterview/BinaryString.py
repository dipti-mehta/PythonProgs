# check if string is binary or not
def check(str):
    p = set(str)
    s = {'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("yes")
    else:
        print("no")

str1 = "1010101010011"
print(check(str1))