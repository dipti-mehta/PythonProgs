# calculate order first then armstrong
def order(a):
    length = 0
    while a != 0:
        length = length + 1
        a = a // 10
    return length


def isArmstrong(a):
    length = order(a)
    sum1 = 0
    tmp = a
    while a != 0:
        lastdigit = a % 10
        sum1 = sum1 + (lastdigit ** length)
        a = a // 10
    if sum1 == tmp:
        return "is Armstrong"
    else:
        return "is not armstrong"


a = 153
print(isArmstrong(a))
