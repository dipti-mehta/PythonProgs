# in a series of numbers from 1 to 100
# some 1 number is missing, how do u find it
# ---------approach 1------------------------
arr = [1,2,4,5]
sumArr = sum(arr)
n = len(arr)+1
totalSum = (n*(n+1)//2)
missingNum = totalSum - sumArr
print("Missing number is",missingNum)

# -----------------approach 2---------------------------
def missarr(arr1):
    arr1.sort()
    for i in range(len(arr1)):
        if arr1[i] != i+1:
            return i+1
    return len(arr)+1

arr1 = [1,2,3,6]
print("missing num is",missarr(arr1))








