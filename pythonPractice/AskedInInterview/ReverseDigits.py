'''Write a program to reverse digits of a number
logic is as follows
num = 4562
rev_num = 0
rev_num = rev_num *10 + num%10 = 2
num = num/10 = 456
rev_num = rev_num *10 + num%10 = 20 + 6 = 26
num = num/10 = 45
rev_num = rev_num *10 + num%10 = 260 + 5 = 265
num = num/10 = 4
rev_num = rev_num *10 + num%10 = 2650 + 4 = 2654
num = num/10 = 0 '''
# Python program to reverse a number

n = 4562
rev = 0

while(n > 0):
    a = n % 10  # last digit
    rev = rev * 10 + a
    n = n // 10  # remaining digit

print(rev)

# alternate way
# Python 3 program to reverse a number

def reversDigits(num):

	# converting number to string
	string = str(num)

	# reversing the string
	string = string[::-1]

	# converting string to integer
	num = int(string)

	# returning integer
	return num

# Driver code
if __name__ == "__main__":

	num = 4562
	print("Reverse of no. is ", reversDigits(num))
