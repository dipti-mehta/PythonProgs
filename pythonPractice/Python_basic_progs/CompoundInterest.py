# A - P = ci
# A = P(1+R/100)^t

def ci(pp, rr, tt):
    a = pp * (pow((1 + rr/100), tt))
    comp_int = a - pp
    return comp_int


p = int(input("Enter principal: "))
r = float(input("enter rate of interest: "))
t = int(input("enter time: "))
print("compound interest is ", ci(p, r, t))

# Python3 program to find compound
# interest for given values.


# def compound_interest(principal, rate, time):
#
# 	# Calculates compound interest
# 	Amount = principal * (pow((1 + rate / 100), time))
# 	CI = Amount - principal
# 	print("Compound interest is", CI)
#
#
# # Driver Code
# compound_interest(10000, 10.25, 5)


# without using pow function----------------------------------------------------
# To find compound interest

# inputs
p= 1200 # principal amount
t= 2	 # time
r= 5.4 # rate
# calculates the compound interest
a=p*(1+(r/100))**t # formula for calculating amount
ci=a-p # compound interest = amount - principal amount
# printing compound interest value
print(ci)

# ci using loop
def compound_interest(principal, rate, time):
	Amount = principal
	for i in range(time):
		Amount = Amount * (1 + rate/100)
	CI = Amount - principal
	print("Compound interest is", CI)
# Driver Code
compound_interest(1200, 5.4, 2)
#This code is contributed by Jyothi pinjala


