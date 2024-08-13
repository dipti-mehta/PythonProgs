def si(p, r, t):
    sim = (p * r * t)/100
    return sim


p = int(input("Enter principal: "))
r = int(input("enter rate of interest: "))
t = int(input("enter time: "))
print("simple interest is ", si(p,r,t))