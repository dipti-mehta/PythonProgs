# Python code to demonstrate string length
# using for loop

# Returns length of string
def findLen(str):
	counter = 0
	for i in str:
		counter += 1
	return counter


str = "geeks"
print(findLen(str))

#-----------------------------------------------------------------------
# find length of sentence chars excluding spaces
sente = "I Am beautiful"
print(sente)
print("length of sentence with spaces is: ", len(sente))
sente = sente.replace(" ","")
print("length of chars of sentence without spaces is ",len(sente))

#--------------------------------------------------------------------------
# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency
# Using isspace() + sum()

# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

# isspace() checks for space
# sum checks count
res = sum(not chr.isspace() for chr in test_str)

# printing result
print("The Characters Frequency avoiding spaces : " + str(res))
